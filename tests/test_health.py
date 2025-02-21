"""Test module for health check endpoints."""

from fastapi.testclient import TestClient

from my_fibonacci.app import app

client = TestClient(app)


def test_liveness_endpoint() -> None:
    """Test the liveness endpoint returns healthy status."""
    response = client.get("/health/live")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data["details"]


def test_readiness_endpoint() -> None:
    """Test the readiness endpoint returns correct status."""
    response = client.get("/health/ready")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ready"
    assert data["details"]["state_initialized"] is True
    assert data["details"]["sequence_available"] is True 