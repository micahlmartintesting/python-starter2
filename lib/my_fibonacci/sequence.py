"""Module for generating Fibonacci sequences."""

import numpy as np
from numpy import ndarray


def fibonacci_sequence(n: int) -> ndarray:
    """Generate a Fibonacci sequence of length n.

    Args:
        n: Length of sequence to generate.

    Returns:
        ndarray: Array containing the Fibonacci sequence.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Sequence length must be non-negative")
    
    if n == 0:
        return np.array([], dtype=np.int64)
    
    sequence = np.zeros(n, dtype=np.int64)  # Use int64 to avoid overflow
    if n > 1:
        sequence[1] = 1
        for i in range(2, n):
            sequence[i] = sequence[i-1] + sequence[i-2]
    
    return sequence


__all__ = ["fibonacci_sequence"]
