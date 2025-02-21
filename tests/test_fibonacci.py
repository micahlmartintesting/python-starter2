"""Test module for fibonacci sequence generation."""

import pytest
from fastapi.testclient import TestClient
from my_fibonacci.app import app, State
from my_fibonacci.sequence import fibonacci_sequence

client = TestClient(app)

# Constants for test values
SEQUENCE_LENGTH = 5
HTTP_200_OK = 200

# Expected Fibonacci sequence values
FIB_0 = 0
FIB_1 = 1
FIB_2 = 1
FIB_3 = 2
FIB_4 = 3


def test_fibonacci_sequence() -> None:
    """Test fibonacci sequence generation."""
    sequence = fibonacci_sequence(SEQUENCE_LENGTH)
    assert len(sequence) == SEQUENCE_LENGTH
    assert sequence[0] == FIB_0
    assert sequence[1] == FIB_1
    assert sequence[2] == FIB_2
    assert sequence[3] == FIB_3
    assert sequence[4] == FIB_4


def test_fibonacci_sequence_edge_cases() -> None:
    """Test fibonacci sequence with edge cases."""
    # Test empty sequence
    assert len(fibonacci_sequence(0)) == 0
    
    # Test single number
    sequence = fibonacci_sequence(1)
    assert len(sequence) == 1
    assert sequence[0] == FIB_0


def test_state_initialization() -> None:
    """Test State class initialization."""
    state = State()
    assert state.current_index == 0
    assert len(state.sequence) == 100  # Default pre-generated length


def test_generate_endpoint() -> None:
    """Test the /generate endpoint returns sequential fibonacci numbers."""
    # First request should return 0
    response = client.get("/generate")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"number": FIB_0}

    # Second request should return 1
    response = client.get("/generate")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"number": FIB_1}

    # Third request should return 1
    response = client.get("/generate")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"number": FIB_2}


def test_generate_endpoint_sequence_extension() -> None:
    """Test that the endpoint extends sequence when needed."""
    state = State()
    # Set index near the end of pre-generated sequence
    state.current_index = 98
    
    # Make requests that should trigger sequence extension
    for _ in range(5):
        response = client.get("/generate")
        assert response.status_code == HTTP_200_OK
        assert "number" in response.json()


def test_fibonacci_sequence_validation() -> None:
    """Test fibonacci sequence with different inputs."""
    # Test negative number
    with pytest.raises(ValueError):
        fibonacci_sequence(-1)
    
    # Test large number
    sequence = fibonacci_sequence(200)
    assert len(sequence) == 200


def test_generate_endpoint_state_management() -> None:
    """Test state management in generate endpoint."""
    # Reset state
    app.state.fibonacci = State()
    
    # Make multiple requests to test state management
    for i in range(150):  # Test beyond initial sequence length
        response = client.get("/generate")
        assert response.status_code == HTTP_200_OK
        data = response.json()
        assert isinstance(data["number"], int)
        if i == 0:
            assert data["number"] == FIB_0
        elif i == 1:
            assert data["number"] == FIB_1
