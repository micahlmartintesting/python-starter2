"""Test module for fibonacci sequence."""

import numpy as np
import pytest
from my_fibonacci.sequence import fibonacci_sequence


def test_fibonacci_sequence() -> None:
    """Test fibonacci sequence generation."""
    # Test negative input
    with pytest.raises(ValueError, match="Sequence length must be non-negative"):
        fibonacci_sequence(-1)

    # Test empty sequence
    assert len(fibonacci_sequence(0)) == 0

    # Test sequence values
    sequence = fibonacci_sequence(5)
    expected = np.array([0, 1, 1, 2, 3], dtype=int)
    np.testing.assert_array_equal(sequence, expected)
