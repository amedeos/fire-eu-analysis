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

# ------------------------------------------------------------
# 3. Install Python dependencies
# ------------------------------------------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ------------------------------------------------------------
# 4. Copy project files (only used when not bind-mounted)
# ------------------------------------------------------------
COPY . .

# ------------------------------------------------------------
# 5. Python path for local modules
# ------------------------------------------------------------
ENV PYTHONPATH=/workspace

# ------------------------------------------------------------
# 6. Default command
# ------------------------------------------------------------
ENTRYPOINT ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--ServerApp.token="]

