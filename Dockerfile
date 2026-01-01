# Use Python 3.14 slim image
FROM python:3.14-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

# Out app's environment settings
ENV SERVER_PORT=8080

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry

# Disable Poetry virtualenvs inside container
RUN poetry config virtualenvs.create false

# Copy dependency files first (for layer caching)
COPY pyproject.toml poetry.lock ./

# Install project dependencies
RUN poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the project
COPY . .

# Copy entrypoint script
COPY docker-entrypoint.sh ./
RUN chmod +x docker-entrypoint.sh

# Expose default port
EXPOSE 8080

# Use entrypoint to run migrations then start app
ENTRYPOINT ["./docker-entrypoint.sh"]
