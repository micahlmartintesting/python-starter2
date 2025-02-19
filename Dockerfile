# Use the official Python image as the base
FROM python:3.12-slim

# Set environment variables
ENV POETRY_VERSION=1.6.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_CREATE=false \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# Update PATH
ENV PATH="$POETRY_HOME/bin:$PATH"

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy project files
COPY pyproject.toml poetry.lock ./

# Install project dependencies
RUN poetry install --no-root --only main

# Copy the rest of the application code
COPY . .

# Expose the port the application runs on (adjust if necessary)
EXPOSE 8000

# Define the command to run the application (adjust if necessary)
CMD ["python", "-m", "my_fibonacci"]

