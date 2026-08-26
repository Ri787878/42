from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
import numpy as np


class Mode(Enum):
    EXPECT_VALUE = auto()
    EXPECT_KEY_OR_END = auto()
    EXPECT_COLON = auto()
    EXPECT_COMMA_OR_END = auto()


class ContainerType(Enum):
    OBJECT = auto()
    ARRAY = auto()


@dataclass
class _Container:
    kind: ContainerType
    expecting_key: bool = False


@dataclass
class JsonState:
    """
    Incremental JSON parser state for constrained decoding.

    Usage:
        s = JsonState.initialize(top_level="any_json_value")
        ok = s.consume(token_text)   # feed generated token text incrementally
        if s.is_complete_json_value(): ...
    """
    # structural state
    stack: list[_Container] = field(default_factory=list)
    mode: Mode = Mode.EXPECT_VALUE
    top_level_done: bool = False
    top_level: str = "any_json_value"  # "any_json_value" or "object_only"

    # string state
    in_string: bool = False
    string_is_key: bool = False
    escape: bool = False
    unicode_left: int = 0

    # literal/number state
    literal_target: str | None = None
    literal_index: int = 0

    number_active: bool = False
    number_seen_digit: bool = False
    number_after_exp: bool = False
    number_seen_exp_digit: bool = False
    number_can_end: bool = False

    error: str | None = None

    @classmethod
    def initialize(cls, top_level: str = "any_json_value") -> "JsonState":
        return cls(top_level=top_level)

    def clone(self) -> "JsonState":
        c = JsonState(
            stack=[_Container(x.kind, x.expecting_key) for x in self.stack],
            mode=self.mode,
            top_level_done=self.top_level_done,
            top_level=self.top_level,
            in_string=self.in_string,
            string_is_key=self.string_is_key,
            escape=self.escape,
            unicode_left=self.unicode_left,
            literal_target=self.literal_target,
            literal_index=self.literal_index,
            number_active=self.number_active,
            number_seen_digit=self.number_seen_digit,
            number_after_exp=self.number_after_exp,
            number_seen_exp_digit=self.number_seen_exp_digit,
            number_can_end=self.number_can_end,
            error=self.error,
        )
        return c

    def can_consume(self, text: str) -> bool:
        tmp = self.clone()
        return tmp.consume(text)

    def is_complete_json_value(self) -> bool:
        return (
            self.top_level_done
            and not self.stack
            and not self.in_string
            and self.literal_target is None
            and not self.number_active
        )

    def consume(self, text: str) -> bool:
        for ch in text:
            if not self._consume_char(ch):
                return False
        return True

    # -------- internals --------

    def _fail(self, msg: str) -> bool:
        self.error = msg
        return False

    def _is_ws(self, ch: str) -> bool:
        return ch in " \t\r\n"

    def _is_hex(self, ch: str) -> bool:
        return ch.isdigit() or ch.lower() in "abcdef"

    def _is_num_start(self, ch: str) -> bool:
        return ch == "-" or ch.isdigit()

    def _start_literal(self, target: str, ch: str) -> bool:
        self.literal_target = target
        self.literal_index = 0
        return self._consume_literal_char(ch)

    def _consume_literal_char(self, ch: str) -> bool:
        assert self.literal_target is not None
        if self.literal_index >= len(self.literal_target):
            return self._fail("literal overflow")
        expected = self.literal_target[self.literal_index]
        if ch != expected:
            return self._fail(
                f"literal mismatch, expected {expected!r}, got {ch!r}")
        self.literal_index += 1
        if self.literal_index == len(self.literal_target):
            self.literal_target = None
            self.literal_index = 0
            self._finish_scalar_value()
        return True

    def _start_number(self, ch: str) -> bool:
        self.number_active = True
        self.number_seen_digit = False
        self.number_after_exp = False
        self.number_seen_exp_digit = False
        self.number_can_end = False
        return self._consume_number_char(ch)

    def _consume_number_char(self, ch: str) -> bool:
        # permissive incremental DFA; enough for constrained decoding
        if ch.isdigit():
            self.number_seen_digit = True
            if self.number_after_exp:
                self.number_seen_exp_digit = True
            self.number_can_end = True
            return True

        if (
             ch == "-"
             and not self.number_seen_digit
             and not self.number_after_exp
             and not self.number_can_end):
            # leading '-'
            return True

        if ch == ".":
            if not self.number_seen_digit or self.number_after_exp:
                return self._fail("invalid '.' in number")
            self.number_can_end = False
            return True

        if ch in "eE":
            if not self.number_seen_digit or self.number_after_exp:
                return self._fail("invalid exponent")
            self.number_after_exp = True
            self.number_seen_exp_digit = False
            self.number_can_end = False
            return True

        if ch in "+-":
            # sign allowed only immediately after exponent
            if (
                 not self.number_after_exp
                 or self.number_seen_exp_digit
                 or self.number_can_end):
                return self._fail("invalid exponent sign")
            return True

        # non-number char => only valid if number can end,
        # then reprocess char in normal flow
        if not self.number_can_end:
            return self._fail("number ended prematurely")
        self.number_active = False
        # number ended; commit value and reprocess current char
        self._finish_scalar_value()
        return self._consume_char(ch, reentered=True)

    def _consume_char(self, ch: str, reentered: bool = False) -> bool:
        if self.error:
            return False

        # once complete, allow only whitespace
        if self.is_complete_json_value():
            if self._is_ws(ch):
                return True
            return self._fail("extra data after complete JSON value")

        # string handling
        if self.in_string:
            if self.unicode_left > 0:
                if not self._is_hex(ch):
                    return self._fail("invalid unicode escape")
                self.unicode_left -= 1
                return True

            if self.escape:
                self.escape = False
                if ch == "u":
                    self.unicode_left = 4
                    return True
                if ch in ['"', "\\", "/", "b", "f", "n", "r", "t"]:
                    return True
                return self._fail("invalid escape sequence")

            if ch == "\\":
                self.escape = True
                return True

            if ch == '"':
                self.in_string = False
                if self.string_is_key:
                    self.string_is_key = False
                    self.mode = Mode.EXPECT_COLON
                else:
                    self._finish_scalar_value()
                return True

            # any char allowed inside string
            # (including whitespace/newlines if model emits them)
            return True

        # literal handling
        if self.literal_target is not None:
            return self._consume_literal_char(ch)

        # number handling
        if self.number_active:
            return self._consume_number_char(ch)

        # whitespace outside tokens
        if self._is_ws(ch):
            return True

        # mode-based parsing
        if self.mode == Mode.EXPECT_VALUE:
            return self._consume_value_start(ch)

        if self.mode == Mode.EXPECT_KEY_OR_END:
            if ch == "}":
                if (
                     not self.stack
                     or self.stack[-1].kind != ContainerType.OBJECT
                     or not self.stack[-1].expecting_key):
                    return self._fail("unexpected '}'")
                self.stack.pop()
                self._container_closed()
                return True
            if ch == '"':
                self.in_string = True
                self.string_is_key = True
                return True
            return self._fail("expected object key string or '}'")

        if self.mode == Mode.EXPECT_COLON:
            if ch == ":":
                self.mode = Mode.EXPECT_VALUE
                return True
            return self._fail("expected ':'")

        if self.mode == Mode.EXPECT_COMMA_OR_END:
            if not self.stack:
                return self._fail("internal: comma/end with empty stack")
            top = self.stack[-1]
            if top.kind == ContainerType.OBJECT:
                if ch == ",":
                    top.expecting_key = True
                    self.mode = Mode.EXPECT_KEY_OR_END
                    return True
                if ch == "}":
                    self.stack.pop()
                    self._container_closed()
                    return True
                return self._fail("expected ',' or '}'")
            else:
                if ch == ",":
                    self.mode = Mode.EXPECT_VALUE
                    return True
                if ch == "]":
                    self.stack.pop()
                    self._container_closed()
                    return True
                return self._fail("expected ',' or ']'")

        return self._fail("unknown mode")

    def _consume_value_start(self, ch: str) -> bool:
        # top-level constraint
        if (
             self.top_level == "object_only"
             and not self.stack
             and not self.top_level_done):
            if ch != "{":
                return self._fail("top-level must be object")

        if ch == "{":
            self.stack.append(
                _Container(ContainerType.OBJECT, expecting_key=True))
            self.mode = Mode.EXPECT_KEY_OR_END
            return True

        if ch == "[":
            self.stack.append(_Container(ContainerType.ARRAY))
            self.mode = Mode.EXPECT_VALUE
            return True

        if ch == '"':
            self.in_string = True
            self.string_is_key = False
            return True

        if ch == "t":
            return self._start_literal("true", ch)

        if ch == "f":
            return self._start_literal("false", ch)

        if ch == "n":
            return self._start_literal("null", ch)

        if self._is_num_start(ch):
            return self._start_number(ch)

        return self._fail("invalid value start")

    def _finish_scalar_value(self) -> None:
        # finished string/number/literal value
        if not self.stack:
            self.top_level_done = True
            return

        top = self.stack[-1]
        if top.kind == ContainerType.OBJECT:
            # just consumed value for a key
            top.expecting_key = False
            self.mode = Mode.EXPECT_COMMA_OR_END
        else:
            # array value completed
            self.mode = Mode.EXPECT_COMMA_OR_END

    def _container_closed(self) -> None:
        # closing object/array yields one completed value in parent context
        if not self.stack:
            self.top_level_done = True
            return

        parent = self.stack[-1]
        if parent.kind == ContainerType.OBJECT:
            parent.expecting_key = False
            self.mode = Mode.EXPECT_COMMA_OR_END
        else:
            self.mode = Mode.EXPECT_COMMA_OR_END


def mask_all_except(
     logits: np.ndarray,
     allowed_ids: set[int],
     value: float = -float("inf")
     ) -> np.ndarray:
    """
    Return a masked copy of logits where indices not in
    allowed_ids are set to `value`.
    
    Expects logits shape [vocab_size].
    """
    arr = np.asarray(logits, dtype=float).copy()
    if arr.ndim != 1:
        raise ValueError(
            f"mask_all_except expects 1D logits, got shape={arr.shape}")

    if not allowed_ids:
        arr[:] = value
        return arr

    mask = np.ones(arr.shape[0], dtype=bool)
    valid = [i for i in allowed_ids if 0 <= i < arr.shape[0]]
    mask[valid] = False
    arr[mask] = value
    return arr


class JsonTokenEnforcer:
    """
    Minimal token-level JSON enforcer:
    - tests each token by simulating JsonState.consume(token_text)
    - returns allowed token ids
    """

    def __init__(
         self,
         token_to_id: dict[str, int],
         eos_token_id: int | None = None
         ):
        self.token_to_id = token_to_id
        self.eos_token_id = eos_token_id

        # Build reverse map once
        self.id_to_token: dict[int, str] = {
            tid: tok for tok, tid in token_to_id.items()
            }

    def allowed_token_ids(
         self,
         state,
         generated_ids: list[int] | None = None
         ) -> set[int]:
        allowed: set[int] = set()

        # If JSON is complete, allow EOS
        # (and optionally whitespace tokens if your vocab has them)
        if state.is_complete_json_value():
            if self.eos_token_id is not None:
                allowed.add(self.eos_token_id)
            return allowed

        for tid, tok_text in self.id_to_token.items():
            trial = state.clone()
            if trial.consume(tok_text):
                allowed.add(tid)

        return allowed
