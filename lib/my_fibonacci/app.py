"""FastAPI application for Fibonacci sequence generation."""

from typing import Any

from fastapi import FastAPI
from numpy import ndarray

from .sequence import fibonacci_sequence

app = FastAPI(title="Fibonacci Generator")


class State:
    """Application state for maintaining fibonacci sequence."""

    def __init__(self) -> None:
        """Initialize state with pre-generated sequence."""
        self.sequence: ndarray = fibonacci_sequence(100)  # Pre-generate sequence
        self.current_index: int = 0


# Initialize app state
app.state.fibonacci = State()


@app.get("/generate")
async def generate() -> dict[str, int]:
    """
    Generate next number in Fibonacci sequence.

    Returns:
        dict[str, int]: Dictionary containing the next Fibonacci number.

    """
    if app.state.fibonacci.current_index >= len(app.state.fibonacci.sequence):
        # Extend sequence if needed
        app.state.fibonacci.sequence = fibonacci_sequence(len(app.state.fibonacci.sequence) + 100)

    number = app.state.fibonacci.sequence[app.state.fibonacci.current_index]
    app.state.fibonacci.current_index += 1
    return {"number": int(number)}
