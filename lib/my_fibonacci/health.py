"""Health check endpoints for the FastAPI application."""

from datetime import datetime
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Response model for health check endpoints."""

    status: str
    details: dict[str, Any]


def get_liveness_response() -> HealthResponse:
    """
    Get liveness check response.

    @return: Current health status
    @rtype: HealthResponse
    """
    return HealthResponse(
        status="healthy", details={"timestamp": datetime.now().isoformat()}
    )


def get_readiness_response(state: FastAPI) -> HealthResponse:
    """
    Get readiness check response.

    @param state: FastAPI application state
    @type state: FastAPI
    @return: Current readiness status
    @rtype: HealthResponse
    """
    checks = {
        "state_initialized": hasattr(state, "fibonacci"),
        "sequence_available": (
            hasattr(state, "fibonacci") and len(state.fibonacci.sequence) > 0
        ),
    }
    return HealthResponse(
        status="ready" if all(checks.values()) else "not_ready", details=checks
    )
