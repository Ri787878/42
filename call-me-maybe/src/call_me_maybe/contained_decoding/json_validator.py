from __future__ import annotations
import numpy as np
import json


class BasicJsonFSM:
    """
    FSM that constrains decoding to a minimal JSON object format:
        {"<key>":"<value>"}

    Assumptions:
    - No escapes inside strings
    - Exactly one key/value pair
    - Key/value must be non-empty
    """

    # State definitions
    STATE_EXPECT_OPEN_BRACE = 0
    STATE_EXPECT_KEY_OPEN_QUOTE = 1
    STATE_EXPECT_KEY_BODY = 2
    STATE_EXPECT_COLON = 3
    STATE_EXPECT_VAL_OPEN_QUOTE = 4
    STATE_EXPECT_VAL_BODY = 5
    STATE_EXPECT_CLOSE_BRACE = 6
    STATE_DONE = 7

    def __init__(self, tokenizer_vocab: dict[str, int]):
        """
        tokenizer_vocab: Mapping from token string -> token id
        """
        self.vocab = tokenizer_vocab
        self.inv_vocab = {v: k for k, v in tokenizer_vocab.items()}
        self.current_state = self.STATE_EXPECT_OPEN_BRACE

        # Track whether we're currently inside a key/value
        # string and if it has content
        self._in_key_string = False
        self._in_val_string = False
        self._key_has_content = False
        self._val_has_content = False

    # -------------------------
    # Token helpers
    # -------------------------
    @staticmethod
    def _normalize_token(token_str: str) -> str:
        # Handles common leading-space markers but preserves punctuation
        # Do not aggressively strip internal chars.
        return token_str.lstrip("Ġ▁ ")

    def _token_contains(self, token_str: str, ch: str) -> bool:
        norm = self._normalize_token(token_str)
        return (ch in norm) or (ch in token_str)

    def _get_tokens_containing(self, ch: str) -> list[int]:
        return [
            token_id
            for token_str, token_id in self.vocab.items()
            if self._token_contains(token_str, ch)
        ]

    def _get_string_content_tokens(self) -> list[int]:
        blocked_chars = {'"', "{", "}", ":"}
        allowed = []

        for token_str, token_id in self.vocab.items():
            norm = self._normalize_token(token_str)

            if not norm.strip():
                continue

            # hard reject any structural char in content tokens
            if (
                any(ch in norm for ch in blocked_chars)
                or any(ch in token_str for ch in blocked_chars)
            ):
                continue

            allowed.append(token_id)

        return allowed

    # -------------------------
    # Public API
    # -------------------------
    def reset(self) -> None:
        self.current_state = self.STATE_EXPECT_OPEN_BRACE
        self._in_key_string = False
        self._in_val_string = False
        self._key_has_content = False
        self._val_has_content = False

    def is_done(self) -> bool:
        return self.current_state == self.STATE_DONE

    def get_allowed_token_ids(self) -> list[int]:
        """Return valid token IDs for current state."""
        if self.current_state == self.STATE_EXPECT_OPEN_BRACE:
            return self._get_tokens_containing("{")

        if self.current_state == self.STATE_EXPECT_KEY_OPEN_QUOTE:
            return self._get_tokens_containing('"')

        if self.current_state == self.STATE_EXPECT_KEY_BODY:
            allowed = self._get_string_content_tokens()
            # Once key has at least one token, allow closing quote too
            if self._key_has_content:
                allowed += self._get_tokens_containing('"')
            return list(set(allowed))

        if self.current_state == self.STATE_EXPECT_COLON:
            return self._get_tokens_containing(":")

        if self.current_state == self.STATE_EXPECT_VAL_OPEN_QUOTE:
            return self._get_tokens_containing('"')

        if self.current_state == self.STATE_EXPECT_VAL_BODY:
            allowed = self._get_string_content_tokens()
            # Once value has at least one token, allow closing quote too
            if self._val_has_content:
                allowed += self._get_tokens_containing('"')
            return list(set(allowed))

        if self.current_state == self.STATE_EXPECT_CLOSE_BRACE:
            return self._get_tokens_containing("}")

        return []

    def update_state(self, selected_token_id: int) -> None:
        """Advance state machine after sampling one token."""
        token_str = self.inv_vocab.get(selected_token_id, "")
        norm = self._normalize_token(token_str)

        has_quote = ('"' in norm) or ('"' in token_str)
        has_open_brace = ("{" in norm) or ("{" in token_str)
        has_close_brace = ("}" in norm) or ("}" in token_str)
        has_colon = (":" in norm) or (":" in token_str)

        if self.current_state == self.STATE_EXPECT_OPEN_BRACE:
            if has_open_brace:
                self.current_state = self.STATE_EXPECT_KEY_OPEN_QUOTE
            return

        if self.current_state == self.STATE_EXPECT_KEY_OPEN_QUOTE:
            if has_quote:
                self.current_state = self.STATE_EXPECT_KEY_BODY
                self._in_key_string = True
                self._key_has_content = False
            return

        if self.current_state == self.STATE_EXPECT_KEY_BODY:
            if has_quote and self._key_has_content:
                # close key string
                self._in_key_string = False
                self.current_state = self.STATE_EXPECT_COLON
            else:
                # treat as content token
                self._key_has_content = True
            return

        if self.current_state == self.STATE_EXPECT_COLON:
            if has_colon:
                self.current_state = self.STATE_EXPECT_VAL_OPEN_QUOTE
            return

        if self.current_state == self.STATE_EXPECT_VAL_OPEN_QUOTE:
            if has_quote:
                self.current_state = self.STATE_EXPECT_VAL_BODY
                self._in_val_string = True
                self._val_has_content = False
            return

        if self.current_state == self.STATE_EXPECT_VAL_BODY:
            if has_quote and self._val_has_content:
                # close value string
                self._in_val_string = False
                self.current_state = self.STATE_EXPECT_CLOSE_BRACE
            else:
                # treat as content token
                self._val_has_content = True
            return

        if self.current_state == self.STATE_EXPECT_CLOSE_BRACE:
            if has_close_brace:
                self.current_state = self.STATE_DONE
            return

        # STATE_DONE -> no-op


def apply_json_mask(logits: np.ndarray, fsm: BasicJsonFSM) -> np.ndarray:
    """
    Masks all logits except those allowed by the FSM.
    """
    masked_logits = np.full_like(logits, fill_value=-np.inf)
    allowed_token_ids = fsm.get_allowed_token_ids()

    # Guard in case allowed list is empty
    if allowed_token_ids:
        masked_logits[allowed_token_ids] = logits[allowed_token_ids]

    return masked_logits


def load_vocab_from_model(llm_model) -> dict[str, int]:
    """
    Reads the vocab file path from the model and
    loads it into a dict[str, int].
    """
    vocab_path = llm_model.get_path_to_vocab_file()

    with open(vocab_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Case 1: Standard JSON map where keys are token
    # strings and values are integer IDs
    # e.g., {"{": 0, "}": 1, ...}
    if isinstance(data, dict):
        return {str(k): int(v) for k, v in data.items()}

    # Case 2: Vocab file is a plain text file
    # (1 token per line, line number = token ID)
    elif isinstance(data, list):
        return {token.strip(): idx for idx, token in enumerate(data)}

    else:
        raise ValueError(f"Unexpected vocab file format at {vocab_path}")
