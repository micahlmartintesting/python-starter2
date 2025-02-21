"""FastAPI application for Fibonacci sequence generation."""

from typing import Any

from fastapi import FastAPI
from numpy import ndarray

from .health import HealthResponse, get_liveness_response, get_readiness_response
from .models import State
from .sequence import (
    INITIAL_SEQUENCE_LENGTH,
    SEQUENCE_EXTENSION_SIZE,
    fibonacci_sequence,
)

app = FastAPI(title="Fibonacci Generator")


# Initialize app state
app.state.fibonacci = State()


@app.get("/health/live", response_model=HealthResponse)
async def liveness() -> HealthResponse:
    """
    Check if the application is alive.

    @return: Current health status
    @rtype: HealthResponse
    """
    return get_liveness_response()


@app.get("/health/ready", response_model=HealthResponse)
async def readiness() -> HealthResponse:
    """
    Check if the application is ready to handle requests.

    @return: Current readiness status
    @rtype: HealthResponse
    """
    return get_readiness_response(app.state)


@app.get("/generate")
async def generate() -> dict[str, int]:
    """
    Generate next number in Fibonacci sequence.

    @return: Dictionary containing the next Fibonacci number
    @rtype: dict[str, int]
    """
    current_length = len(app.state.fibonacci.sequence)
    if app.state.fibonacci.current_index >= current_length:
        # Extend sequence if needed
        new_length = current_length + SEQUENCE_EXTENSION_SIZE
        app.state.fibonacci.sequence = fibonacci_sequence(new_length)

    number = app.state.fibonacci.sequence[app.state.fibonacci.current_index]
    app.state.fibonacci.current_index += 1
    return {"number": int(number)}
