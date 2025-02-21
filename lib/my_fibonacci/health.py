"""Health check endpoints for the FastAPI application."""

from datetime import datetime
from typing import Any

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Response model for health check endpoints."""

    status: str
    details: dict[str, Any]


def get_liveness_response() -> HealthResponse:
    """Get liveness check response.

    Returns:
        HealthResponse: Current health status
    """
    return HealthResponse(
        status="healthy",
        details={"timestamp": datetime.now().isoformat()}
    )


def get_readiness_response(state: Any) -> HealthResponse:
    """Get readiness check response.

    Args:
        state: Application state to check

    Returns:
        HealthResponse: Current readiness status
    """
    checks = {
        "state_initialized": hasattr(state, "fibonacci"),
        "sequence_available": (
            hasattr(state, "fibonacci") and 
            len(state.fibonacci.sequence) > 0
        )
    }
    return HealthResponse(
        status="ready" if all(checks.values()) else "not_ready",
        details=checks
    ) 