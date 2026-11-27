from llm_sdk import Small_LLM_Model
from pydantic import BaseModel
import json
from copy import copy
import re

import numpy as np


class BasicJsonFSM(BaseModel):
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
    STATE_IN_NUMBER = 10

    VALID_ESCAPES = set('"\\/bfnrt')
    HEX_DIGITS = set("0123456789abcdefABCDEF")

    def __init__(
        self,
        tokenizer_vocab: dict[str, int],
        function_schemas: dict[str, dict[str, str]],
    ):
        """Initialize the JSON FSM with a tokenizer vocabulary and schemas."""
        self.function_schemas = function_schemas
        self.selected_function: str | None = None
        self.vocab = tokenizer_vocab
        self.root_keys_seen: frozenset[str] = frozenset()
        self.parameter_keys_seen: frozenset[str] = frozenset()
        self.string_buffer = ""
        self.expecting_key_after_comma = False
        self.inv_vocab = {
            token_id: token
            for token, token_id in tokenizer_vocab.items()
        }

        self.normalized_vocab = {
            token_id: self._normalize_token(token)
            for token_id, token in self.inv_vocab.items()
        }
        self._allowed_cache: dict[tuple, tuple[int, ...]] = {}

        self.current_state = self.STATE_EXPECT_OPEN_BRACE
        self.object_depth = 0
        self.string_kind: str | None = None
        self.string_has_content = False
        self.unicode_digits_remaining = 0
        self.current_key = ""
        self.number_buffer = ""

    @staticmethod
    def _normalize_token(token: str) -> str:
        """
        Convert common tokenizer space markers to normal spaces.

        Leading normal spaces are preserved because spaces can be meaningful
        inside JSON string values.
        """
        return token.replace("Ġ", " ").replace("▁", " ")

    def _expected_keys(self) -> frozenset[str]:
        """Return the keys permitted in the current JSON object."""
        if self.object_depth == 1:
            if self.selected_function is None:
                return frozenset({"name"} - self.root_keys_seen)
            return frozenset({"name", "parameters"} - self.root_keys_seen)

        if self.object_depth == 2 and self.selected_function is not None:
            parameter_names = self.function_schemas[self.selected_function]
            return frozenset(parameter_names) - self.parameter_keys_seen

        return frozenset()

    def _object_is_complete(self) -> bool:
        """Return whether the current object contains all required keys."""
        if self.object_depth == 1:
            return self.root_keys_seen == frozenset({"name", "parameters"})

        if self.object_depth == 2 and self.selected_function is not None:
            return self.parameter_keys_seen == frozenset(
                self.function_schemas[self.selected_function]
            )

        return False

    def _close_object(self) -> bool:
        """
        Close the current object if it is complete and has no trailing comma.
        """
        if self.expecting_key_after_comma or not self._object_is_complete():
            return False

        self.object_depth -= 1
        self.current_state = (
            self.STATE_DONE
            if self.object_depth == 0
            else self.STATE_AFTER_VALUE
        )
        return True

    def _current_parameter_type(self) -> str | None:
        """
        Return the expected type of the current function parameter, if any.
        """
        if self.object_depth != 2 or self.selected_function is None:
            return None

        return (
            self.function_schemas[self.selected_function].get(self.current_key)
        )

    def reset(self) -> None:
        """
        Reset the FSM to its initial state for a new JSON generation.
        """
        self.current_state = self.STATE_EXPECT_OPEN_BRACE
        self.object_depth = 0
        self.string_kind = None
        self.string_has_content = False
        self.unicode_digits_remaining = 0
        self.current_key = ""
        self.number_buffer = ""
        self._allowed_cache.clear()
        self.selected_function = None
        self.root_keys_seen = frozenset()
        self.parameter_keys_seen = frozenset()
        self.string_buffer = ""
        self.expecting_key_after_comma = False

    def _number_is_valid(self) -> bool:
        """Return whether the buffered text matches JSON number syntax."""
        try:
            value = json.loads(
                self.number_buffer,
                parse_constant=lambda _: None
            )
        except json.JSONDecodeError:
            return False

        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def _finish_number_delimiter(self, character: str) -> bool:
        """Finish a valid number and process the character that follows it."""
        if not self._number_is_valid():
            return False

        if character == "}":
            if not self._close_object():
                return False
        elif character == ",":
            self.current_state = self.STATE_EXPECT_KEY_OR_CLOSE
            self.expecting_key_after_comma = True
        else:
            self.current_state = self.STATE_AFTER_VALUE

        self.number_buffer = ""
        return True

    def is_done(self) -> bool:
        """Check if json is done"""
        return self.current_state == self.STATE_DONE

    def _consume_character(self, character: str) -> bool:
        """Function checks if it can consume a charecter"""
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
                return self._close_object()

            if character == '"' and self._expected_keys():
                self.string_kind = "key"
                self.string_has_content = False
                self.current_key = ""
                self.expecting_key_after_comma = False
                self.current_state = self.STATE_IN_STRING
                return True

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

            if self.object_depth == 1 and self.current_key == "name":
                if character == '"':
                    self.string_kind = "function_name"
                    self.string_buffer = ""
                    self.current_state = self.STATE_IN_STRING
                    return True
                return False

            if self.object_depth == 1 and self.current_key == "parameters":
                if character == "{" and self.selected_function is not None:
                    self.object_depth += 1
                    self.current_state = self.STATE_EXPECT_KEY_OR_CLOSE
                    return True
                return False

            parameter_type = self._current_parameter_type()

            if parameter_type == "string" and character == '"':
                self.string_kind = "value"
                self.current_state = self.STATE_IN_STRING
                return True

            if parameter_type == "number" and (
                character == "-" or character.isdigit()
            ):
                self.number_buffer = character
                self.current_state = self.STATE_IN_NUMBER
                return True

            return False

        if self.current_state == self.STATE_IN_KEY:
            return False

        if self.current_state == self.STATE_IN_STRING:
            if character == '"':
                if self.string_kind == "key":
                    if self.current_key not in self._expected_keys():
                        return False

                    if self.object_depth == 1:
                        self.root_keys_seen |= {self.current_key}
                    else:
                        self.parameter_keys_seen |= {self.current_key}

                    self.current_state = self.STATE_EXPECT_COLON

                elif self.string_kind == "function_name":
                    if self.string_buffer not in self.function_schemas:
                        return False

                    self.selected_function = self.string_buffer
                    self.current_state = self.STATE_AFTER_VALUE

                else:
                    self.current_state = self.STATE_AFTER_VALUE

                self.string_kind = None
                return True

            if self.string_kind == "key":
                candidate_key = self.current_key + character
                if not any(
                    key.startswith(candidate_key)
                    for key in self._expected_keys()
                ):
                    return False
                self.current_key = candidate_key

            elif self.string_kind == "function_name":
                if character == "\\":
                    return False

                candidate_name = self.string_buffer + character
                if not any(
                    name.startswith(candidate_name)
                    for name in self.function_schemas
                ):
                    return False
                self.string_buffer = candidate_name

            if character == "\\":
                self.current_state = self.STATE_IN_ESCAPE
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

        if self.current_state == self.STATE_IN_NUMBER:
            if character.isspace() or character in ",}":
                return self._finish_number_delimiter(character)

            if character.isdigit():
                self.number_buffer += character
                return True

            if character == "-" and ("e" in self.number_buffer.lower()):
                if self.number_buffer.lower().endswith(("e", "E")):
                    self.number_buffer += character
                    return True
                return False

            if character in "+" and ("e" in self.number_buffer.lower()):
                if self.number_buffer.lower().endswith(("e", "E")):
                    self.number_buffer += character
                    return True
                return False

            if character == ".":
                if (
                    "." not in self.number_buffer
                    and "e" not in self.number_buffer.lower()
                ):
                    self.number_buffer += character
                    return True
                return False

            if character in "eE":
                if (
                    "e" not in self.number_buffer.lower()
                    and "." not in self.number_buffer
                    or (
                        "e" not in self.number_buffer.lower()
                        and "." in self.number_buffer
                        and self.number_buffer.endswith(tuple("0123456789"))
                    )
                ):
                    if (
                        re.fullmatch(
                            r'-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?',
                            self.number_buffer
                        )
                    ):
                        self.number_buffer += character
                        return True
                return False

            return False

        if self.current_state == self.STATE_AFTER_VALUE:
            if character.isspace():
                return True

            if character == ",":
                self.current_state = self.STATE_EXPECT_KEY_OR_CLOSE
                self.expecting_key_after_comma = True
                return True

            if character == "}":
                return self._close_object()

            return False

        return False

    def _token_is_allowed(self, token_id: int) -> bool:
        """Function checks if token is allowed"""
        token = self.normalized_vocab.get(token_id)

        if token is None:
            return False

        candidate = copy(self)

        for character in token:
            if not candidate._consume_character(character):
                return False

        return True

    def get_allowed_token_ids(self) -> list[int]:
        """Function returns list of ints of allowed token ids"""
        if self.is_done():
            return []

        key = (
            self.current_state,
            self.object_depth,
            self.string_kind,
            self.string_has_content,
            self.unicode_digits_remaining,
            self.current_key,
            self.number_buffer,
            self.selected_function,
            self.root_keys_seen,
            self.parameter_keys_seen,
            self.string_buffer,
            self.expecting_key_after_comma,
        )
        if key not in self._allowed_cache:
            self._allowed_cache[key] = tuple(
                token_id
                for token_id in self.inv_vocab
                if self._token_is_allowed(token_id)
            )
        return list(self._allowed_cache[key])

    def update_state(self, selected_token_id: int) -> None:
        """
        Advance the JSON parser state using a model-selected token.
        The token is processed character by character, updating this FSM in
        place.
        """
        token = self.normalized_vocab.get(selected_token_id)

        if token is None:
            raise ValueError(
                f"Unknown token ID returned by model: {selected_token_id}"
            )

        for character in token:
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


def select_json_token(logits: np.ndarray, fsm: BasicJsonFSM) -> int:
    """Choose the highest-scoring valid token without scanning the vocabulary.

    Try up to 16 candidates in score order, preserving NumPy's lowest-ID tie
    breaking. Fall back to the cached full mask for restrictive parser states.
    Candidate checks use a copy of the FSM and never advance the real parser.
    """
    scores = logits
    for attempt in range(16):
        token_id = int(np.argmax(scores))
        if not np.isfinite(scores[token_id]):
            break
        if fsm._token_is_allowed(token_id):
            return token_id
        if attempt == 0:
            scores = logits.copy()
        scores[token_id] = -np.inf

    allowed_token_ids = fsm.get_allowed_token_ids()

    if not allowed_token_ids:
        probe = copy(fsm)
        can_consume_n = probe._consume_character("n")

        raise ValueError(
            "No JSON tokens are allowed. "
            f"state={fsm.current_state}, depth={fsm.object_depth}, "
            f"selected_function={fsm.selected_function!r}, "
            f"current_key={fsm.current_key!r}, "
            f"root_keys_seen={fsm.root_keys_seen}, "
            f"parameter_keys_seen={fsm.parameter_keys_seen}, "
            f"string_kind={fsm.string_kind!r}, "
            f"expected_keys={fsm._expected_keys()}, "
            f"can_consume_n={can_consume_n}"
        )

    masked_logits = apply_json_mask(logits, fsm)
    if not np.isfinite(masked_logits).any():
        raise ValueError(
            "Allowed JSON tokens have no finite model logits. "
            f"allowed_count={len(allowed_token_ids)}, "
            f"state={fsm.current_state}, depth={fsm.object_depth}, "
            f"selected_function={fsm.selected_function!r}, "
            f"current_key={fsm.current_key!r}"
        )

    return int(np.argmax(masked_logits))


def load_vocab_from_model(llm_model: Small_LLM_Model) -> dict[str, int]:
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
