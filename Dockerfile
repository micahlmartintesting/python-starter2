# Use the official Python image as the base
FROM python:3.12-slim

# Add base image labels
LABEL org.opencontainers.image.base.name="python:3.12-slim"
LABEL org.opencontainers.image.base.digest="sha256:34656cd90456349040784165b9decccbcee4de66f3ead0a1168ba893455afd1e"

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml, poetry.lock, and README.md files
COPY pyproject.toml poetry.lock README.md ./

# Install Poetry
RUN pip install poetry

# Install dependencies without dev dependencies
RUN poetry install --only main --no-root

# Copy the built artifacts from the pipeline
COPY dist/*.whl ./

# Install the application package
RUN pip install *.whl

# Expose the port the application runs on (adjust if necessary)
EXPOSE 8000

# Define the command to run the application (adjust if necessary)
CMD ["python", "-m", "my_fibonacci"]
