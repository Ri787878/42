from __future__ import annotations

import json
from copy import copy

import numpy as np


class BasicJsonFSM:
    """
    Constrained decoder for JSON objects containing strings and nested objects.

    Supported structure:

        {
          "key": "value",
          "nested": {
            "key": "value"
          }
        }

    Tokens are validated character by character, so multi-character tokenizer
    tokens are handled correctly.
    """

    STATE_EXPECT_OPEN_BRACE = 0
    STATE_EXPECT_KEY_OR_CLOSE = 1
    STATE_IN_KEY = 2
    STATE_EXPECT_COLON = 3
    STATE_EXPECT_VALUE = 4
    STATE_IN_STRING = 5
    STATE_IN_ESCAPE = 6
    STATE_IN_UNICODE_ESCAPE = 7
    STATE_AFTER_VALUE = 8
    STATE_DONE = 9

    VALID_ESCAPES = set('"\\/bfnrt')
    HEX_DIGITS = set("0123456789abcdefABCDEF")

    def __init__(self, tokenizer_vocab: dict[str, int]):
        self.vocab = tokenizer_vocab
        self.inv_vocab = {
            token_id: token
            for token, token_id in tokenizer_vocab.items()
        }

        self.current_state = self.STATE_EXPECT_OPEN_BRACE
        self.object_depth = 0
        self.string_kind: str | None = None
        self.string_has_content = False
        self.unicode_digits_remaining = 0

    @staticmethod
    def _normalize_token(token: str) -> str:
        """
        Convert common tokenizer space markers to normal spaces.

        Leading normal spaces are preserved because spaces can be meaningful
        inside JSON string values.
        """
        return token.replace("Ġ", " ").replace("▁", " ")

    def reset(self) -> None:
        self.current_state = self.STATE_EXPECT_OPEN_BRACE
        self.object_depth = 0
        self.string_kind = None
        self.string_has_content = False
        self.unicode_digits_remaining = 0

    def is_done(self) -> bool:
        return self.current_state == self.STATE_DONE

    def _is_inside_string(self) -> bool:
        return self.current_state in {
            self.STATE_IN_STRING,
            self.STATE_IN_ESCAPE,
            self.STATE_IN_UNICODE_ESCAPE,
        }

    def _consume_character(self, character: str) -> bool:
        if self.current_state == self.STATE_DONE:
            return False

        if self.current_state == self.STATE_EXPECT_OPEN_BRACE:
            if character == "{":
                self.object_depth = 1
                self.current_state = self.STATE_EXPECT_KEY_OR_CLOSE
                return True

            return False

        if self.current_state == self.STATE_EXPECT_KEY_OR_CLOSE:
            if character.isspace():
                return True

            if character == "}":
                if self.object_depth == 1:
                    self.object_depth = 0
                    self.current_state = self.STATE_DONE
                    return True

                return False

            if character == '"':
                self.string_kind = "key"
                self.string_has_content = False
                self.current_state = self.STATE_IN_STRING
                return True

            return False

        if self.current_state == self.STATE_IN_KEY:
            return False

        if self.current_state == self.STATE_EXPECT_COLON:
            if character.isspace():
                return True

            if character == ":":
                self.current_state = self.STATE_EXPECT_VALUE
                return True

            return False

        if self.current_state == self.STATE_EXPECT_VALUE:
            if character.isspace():
                return True

            if character == '"':
                self.string_kind = "value"
                self.string_has_content = False
                self.current_state = self.STATE_IN_STRING
                return True

            if character == "{":
                self.object_depth += 1
                self.current_state = self.STATE_EXPECT_KEY_OR_CLOSE
                return True

            return False

        if self.current_state == self.STATE_IN_STRING:
            if character == '"':
                if self.string_kind == "key":
                    self.current_state = self.STATE_EXPECT_COLON
                else:
                    self.current_state = self.STATE_AFTER_VALUE

                self.string_kind = None
                return True

            if character == "\\":
                self.current_state = self.STATE_IN_ESCAPE
                self.string_has_content = True
                return True

            if ord(character) < 0x20:
                return False

            self.string_has_content = True
            return True

        if self.current_state == self.STATE_IN_ESCAPE:
            if character in self.VALID_ESCAPES:
                self.current_state = self.STATE_IN_STRING
                return True

            if character == "u":
                self.unicode_digits_remaining = 4
                self.current_state = self.STATE_IN_UNICODE_ESCAPE
                return True

            return False

        if self.current_state == self.STATE_IN_UNICODE_ESCAPE:
            if character not in self.HEX_DIGITS:
                return False

            self.unicode_digits_remaining -= 1

            if self.unicode_digits_remaining == 0:
                self.current_state = self.STATE_IN_STRING

            return True

        if self.current_state == self.STATE_AFTER_VALUE:
            if character.isspace():
                return True

            if character == ",":
                self.current_state = self.STATE_EXPECT_KEY_OR_CLOSE
                return True

            if character == "}":
                self.object_depth -= 1

                if self.object_depth == 0:
                    self.current_state = self.STATE_DONE
                else:
                    self.current_state = self.STATE_AFTER_VALUE

                return True

            return False

        return False

    def _token_is_allowed(self, token_id: int) -> bool:
        token = self.inv_vocab.get(token_id)

        if token is None:
            return False

        candidate = copy(self)

        for character in self._normalize_token(token):
            if not candidate._consume_character(character):
                return False

        return True

    def get_allowed_token_ids(self) -> list[int]:
        if self.is_done():
            return []
    
        return [
            token_id
            for token_id in self.inv_vocab
            if self._token_is_allowed(token_id)
        ]

    def update_state(self, selected_token_id: int) -> None:
        token = self.inv_vocab.get(selected_token_id)

        if token is None:
            raise ValueError(
                f"Unknown token ID returned by model: {selected_token_id}"
            )

        for character in self._normalize_token(token):
            if not self._consume_character(character):
                raise ValueError(
                    f"Token {selected_token_id} would create invalid JSON: "
                    f"{token!r}"
                )


def apply_json_mask(
    logits: np.ndarray,
    fsm: BasicJsonFSM,
) -> np.ndarray:
    """
    Keep logits only for tokens that preserve valid JSON structure.
    """
    masked_logits = np.full_like(logits, -np.inf)
    allowed_token_ids = fsm.get_allowed_token_ids()

    if allowed_token_ids:
        masked_logits[allowed_token_ids] = logits[allowed_token_ids]

    return masked_logits


def load_vocab_from_model(llm_model) -> dict[str, int]:
    """
    Load a tokenizer vocabulary from the model's vocabulary file.
    """
    vocab_path = llm_model.get_path_to_vocab_file()

    with open(vocab_path, "r", encoding="utf-8") as vocabulary_file:
        data = json.load(vocabulary_file)

    if isinstance(data, dict):
        return {
            str(token): int(token_id)
            for token, token_id in data.items()
        }

    if isinstance(data, list):
        if data and isinstance(data[0], dict):
            return {
                str(item["token"]): int(item["id"])
                for item in data
            }

        return {
            str(token): index
            for index, token in enumerate(data)
        }

    raise ValueError(f"Unexpected vocabulary format at {vocab_path}")
