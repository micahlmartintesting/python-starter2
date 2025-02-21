"""Main entry point for the Fibonacci web server."""

import uvicorn


def main() -> None:
    """Start the FastAPI server."""
    uvicorn.run("my_fibonacci.app:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
