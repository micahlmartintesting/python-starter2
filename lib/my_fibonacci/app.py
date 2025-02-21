"""FastAPI application for Fibonacci sequence generation."""

from typing import Any

from fastapi import FastAPI
from numpy import ndarray

from .sequence import (
    INITIAL_SEQUENCE_LENGTH,
    SEQUENCE_EXTENSION_SIZE,
    fibonacci_sequence,
)

app = FastAPI(title="Fibonacci Generator")


class State:

    """Application state for maintaining fibonacci sequence."""

    def __init__(self) -> None:
        """Initialize state with pre-generated sequence."""
        self.sequence: ndarray = fibonacci_sequence(INITIAL_SEQUENCE_LENGTH)
        self.current_index: int = 0


# Initialize app state
app.state.fibonacci = State()


@app.get("/generate")
async def generate() -> dict[str, int]:
    """
    Generate next number in Fibonacci sequence.

    :returns: Dictionary containing the next Fibonacci number
    :rtype: dict[str, int]
    """
    current_length = len(app.state.fibonacci.sequence)
    if app.state.fibonacci.current_index >= current_length:
        # Extend sequence if needed
        new_length = current_length + SEQUENCE_EXTENSION_SIZE
        app.state.fibonacci.sequence = fibonacci_sequence(new_length)

    number = app.state.fibonacci.sequence[app.state.fibonacci.current_index]
    app.state.fibonacci.current_index += 1
    return {"number": int(number)}
