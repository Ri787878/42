from typing import Dict, Iterable, List, Optional


class SimpleBanningProcessor:
    """
    Pure-Python logits processor that bans configured tokens
    by setting their score to -inf.

    This class is framework-agnostic:
    - No PyTorch
    - No transformers
    - No Hugging Face
    - No DSPy
    """

    def __init__(
        self,
        token_to_id: Dict[str, int],
        words_to_ban: Iterable[str],
        unknown_token_policy: str = "ignore",
    ):
        """
        Args:
            token_to_id:
                Mapping from token string -> integer token id.
            words_to_ban:
                Iterable of tokens (strings) to ban.
            unknown_token_policy:
                - "ignore": skip words not present in token_to_id
                - "error": raise ValueError if a word is unknown
        """
        if unknown_token_policy not in {"ignore", "error"}:
            raise ValueError(
                "unknown_token_policy must be 'ignore' or 'error'")

        self.banned_ids: List[int] = []
        for w in words_to_ban:
            if w in token_to_id:
                self.banned_ids.append(token_to_id[w])
            elif unknown_token_policy == "error":
                raise ValueError(f"Unknown token in words_to_ban: {w!r}")

        # Deduplicate for efficiency
        self.banned_ids = sorted(set(self.banned_ids))

    def __call__(
        self,
        input_ids: Optional[List[List[int]]],
        scores: List[List[float]],
    ) -> List[List[float]]:
        """
        Mutates and returns `scores`.

        Args:
            input_ids:
                Batch of token-id sequences
            scores:
                2D list: scores[batch_index][token_id] = logit/score
                for next token.

        Returns:
            The same `scores` object with banned token positions set to -inf.
        """
        neg_inf = float("-inf")

        for row in scores:
            for token_id in self.banned_ids:
                if 0 <= token_id < len(row):
                    row[token_id] = neg_inf

        return scores
