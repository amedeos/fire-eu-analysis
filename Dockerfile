# fire-eu-analysis Dockerfile
# Multi-stage build to reduce final image size

# Stage 1: Build stage (with build tools)
FROM python:3.12-slim AS builder

# Set locale and non-interactive mode
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Copy requirements
COPY requirements.txt .
COPY requirements-ci.txt .

# Install Python dependencies
ARG CI_BUILD=false
RUN if [ "$CI_BUILD" = "true" ]; then \
      echo "Using lightweight CI requirements (requirements-ci.txt)"; \
      pip install --no-cache-dir --user -r requirements-ci.txt; \
    else \
      echo "Using full requirements (requirements.txt)"; \
      pip install --no-cache-dir --user -r requirements.txt; \
    fi

# Stage 2: Runtime stage (without build tools)
FROM python:3.12-slim

# Set locale and non-interactive mode
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Install only runtime dependencies (git for some packages, but not build-essential)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy Python packages from builder
COPY --from=builder /root/.local /root/.local

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Set working directory
WORKDIR /workspace

# Copy project files (only used when not bind-mounted)
COPY . .

# Python path for local modules
ENV PYTHONPATH=/workspace

# Copy startup script and set permissions
COPY start-jupyter.sh /usr/local/bin/start-jupyter.sh
RUN chmod +x /usr/local/bin/start-jupyter.sh

# Default command
# Start Jupyter Lab with token generation for remote access
# Token will be saved to /workspace/.jupyter_token
ENTRYPOINT ["/usr/local/bin/start-jupyter.sh"]

