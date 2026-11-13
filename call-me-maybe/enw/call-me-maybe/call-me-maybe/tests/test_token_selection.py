"""Regression checks that require NumPy but never load the model or Torch."""
import importlib.util
from pathlib import Path
import unittest

import numpy as np


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "src/call_me_maybe/contained_decoding/json_validator.py"
)
SPEC = importlib.util.spec_from_file_location("json_validator", MODULE_PATH)
DECODER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DECODER)


class TokenSelectionTests(unittest.TestCase):
    def setUp(self):
        tokens = list('{}":, abcdef0123456789\\un')
        tokens += [f"word{i}" for i in range(40)]
        tokens += ['\\u00', 'Ġword', '▁word', '":"', '"}']
        self.vocab = {token: i for i, token in enumerate(dict.fromkeys(tokens))}
        self.fsm = DECODER.BasicJsonFSM(self.vocab)

    def assert_matches_mask(self, scores):
        masked = DECODER.apply_json_mask(scores, self.fsm)
        actual = DECODER.select_json_token(scores, self.fsm)
        self.assertEqual(actual, int(np.argmax(masked)))
        np.testing.assert_array_equal(scores, self.original_scores)
        return actual

    def test_random_scores_across_parser_states(self):
        rng = np.random.default_rng(42)
        # Include string, nested object, escape and Unicode parser states.
        for text in ['{"a":"\\u0041\\n"}', '{"a":{"b":"c"}}']:
            self.fsm.reset()
            for character in text:
                for _ in range(10):
                    scores = rng.normal(size=len(self.vocab))
                    self.original_scores = scores.copy()
                    self.assert_matches_mask(scores)
                self.fsm.update_state(self.vocab[character])
            self.assertTrue(self.fsm.is_done())

    def test_valid_top_token_never_builds_full_mask(self):
        scores = np.zeros(len(self.vocab))
        scores[self.vocab['{']] = 10
        self.assertEqual(DECODER.select_json_token(scores, self.fsm), self.vocab['{'])
        self.assertEqual(self.fsm._allowed_cache, {})
        self.assertEqual(self.fsm.object_depth, 0)

    def test_restrictive_state_falls_back_and_preserves_ties(self):
        # More than 16 invalid higher-scoring candidates force the fallback.
        scores = np.full(len(self.vocab), 10.0)
        scores[self.vocab['{']] = 1
        self.original_scores = scores.copy()
        self.assert_matches_mask(scores)
        self.assertTrue(self.fsm._allowed_cache)
        self.fsm.update_state(self.vocab['{'])
        self.original_scores = np.zeros(len(self.vocab))
        self.assert_matches_mask(self.original_scores.copy())

    def test_no_finite_valid_token_raises(self):
        with self.assertRaises(ValueError):
            DECODER.select_json_token(np.full(len(self.vocab), -np.inf), self.fsm)
        self.fsm.current_state = self.fsm.STATE_DONE
        with self.assertRaises(ValueError):
            DECODER.select_json_token(np.zeros(len(self.vocab)), self.fsm)


if __name__ == "__main__":
    unittest.main()
