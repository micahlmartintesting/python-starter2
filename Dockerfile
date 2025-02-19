# Use the official Python image as the base
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install poetry

# Install dependencies without dev dependencies
RUN poetry install --no-dev --no-root

# Copy the built artifacts from the pipeline
COPY dist/*.whl ./

# Install the application package
RUN pip install *.whl

# Expose the port the application runs on (adjust if necessary)
EXPOSE 8000

# Define the command to run the application (adjust if necessary)
CMD ["python", "-m", "my_fibonacci"]
