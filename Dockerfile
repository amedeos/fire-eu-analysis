# fire-eu-analysis Dockerfile

FROM python:3.12-slim

# Set locale and non-interactive mode
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# ------------------------------------------------------------
# 1. Install system packages
# ------------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------------------------------------
# 2. Set working directory
# ------------------------------------------------------------
WORKDIR /workspace

# 3. Install Python dependencies
# ------------------------------------------------------------
COPY requirements.txt .
COPY requirements-ci.txt .

ARG CI_BUILD=false
RUN if [ "$CI_BUILD" = "true" ]; then \
      echo "Using lightweight CI requirements (requirements-ci.txt)"; \
      pip install --no-cache-dir -r requirements-ci.txt; \
    else \
      echo "Using full requirements (requirements.txt)"; \
      pip install --no-cache-dir -r requirements.txt; \
    fi


# ------------------------------------------------------------
# 4. Copy project files (only used when not bind-mounted)
# ------------------------------------------------------------
COPY . .

# ------------------------------------------------------------
# 5. Python path for local modules
# ------------------------------------------------------------
ENV PYTHONPATH=/workspace

# ------------------------------------------------------------
# 6. Copy startup script and set permissions
# ------------------------------------------------------------
COPY start-jupyter.sh /usr/local/bin/start-jupyter.sh
RUN chmod +x /usr/local/bin/start-jupyter.sh

# ------------------------------------------------------------
# 7. Default command
# Start Jupyter Lab with token generation for remote access
# Token will be saved to /workspace/.jupyter_token
# ------------------------------------------------------------
ENTRYPOINT ["/usr/local/bin/start-jupyter.sh"]

