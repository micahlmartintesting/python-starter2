"""FastAPI application for Fibonacci sequence generation."""

from fastapi import FastAPI
from .fibonacci import fibonacci_sequence

app = FastAPI(title="Fibonacci Generator")

# Store state
class State:
    """Application state."""
    def __init__(self):
        self.sequence = fibonacci_sequence(100)  # Pre-generate sequence
        self.current_index = 0

state = State()

@app.get("/generate")
async def generate():
    """Generate next number in Fibonacci sequence."""
    if state.current_index >= len(state.sequence):
        # Extend sequence if needed
        state.sequence.extend(fibonacci_sequence(len(state.sequence) + 100))
    
    number = state.sequence[state.current_index]
    state.current_index += 1
    return {"number": int(number)}  # Convert numpy int to regular int for JSON 