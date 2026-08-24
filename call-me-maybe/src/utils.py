import numpy as np
import sys


def print_to_stderr(*a):
    """Print a message to stderr"""
    print(*a, file=sys.stderr)


def softmax(x):
    # Subtracting the max value for numerical stability
    exp_x = np.exp(x - np.max(x))
    # Dividing by the sum of exponentials to normalize the values
    return exp_x / exp_x.sum(axis=0)


def softmax_batch(x):
    # Subtracting the max value along each row (axis=1) for stability
    exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    # Dividing by the row-wise sum of exponentials
    return exp_x / exp_x.sum(axis=1, keepdims=True)


def decoding_strategy(probs: np.ndarray) -> int:
    return int(np.argmax(probs))
