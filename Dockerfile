# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the pre-built wheel file(s) from the pipeline artifact.
# Ensure that your CI/CD pipeline includes the "dist" directory in the build context.
COPY dist/*.whl /app/

# Upgrade pip (optional but recommended)
RUN pip install --upgrade pip

# Install the package from the wheel file.
# This installs your project along with its dependencies as declared in the wheel metadata.
RUN pip install /app/*.whl

# Expose a port if your application needs one (adjust as needed)
EXPOSE 8000

# Use the installed command-line script (as defined in pyproject.toml)
CMD ["my_fibonacci"]
