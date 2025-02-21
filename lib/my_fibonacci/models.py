"""Models for the Fibonacci application."""

from numpy import ndarray

from .sequence import INITIAL_SEQUENCE_LENGTH, fibonacci_sequence


class State:
    """Application state for maintaining fibonacci sequence."""

    def __init__(self) -> None:
        """Initialize state with pre-generated sequence."""
        self.sequence: ndarray = fibonacci_sequence(INITIAL_SEQUENCE_LENGTH)
        self.current_index: int = 0
