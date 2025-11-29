#!/usr/bin/env bash
# Start Jupyter Lab in local virtual environment

set -euo pipefail

VENV_DIR="${VENV_DIR:-venv}"
JUPYTER_PORT="${JUPYTER_PORT:-8889}"

# Check if virtual environment exists
if [ ! -d "${VENV_DIR}" ]; then
    echo "[ERROR] Virtual environment '${VENV_DIR}' not found." >&2
    echo "Run './setup-local-env.sh' first to create it." >&2
    exit 1
fi

# Activate virtual environment
source "${VENV_DIR}/bin/activate"

# Check if Jupyter is installed
if ! command -v jupyter >/dev/null 2>&1; then
    echo "[ERROR] Jupyter not found in virtual environment." >&2
    echo "Run './setup-local-env.sh' to install dependencies." >&2
    exit 1
fi

# Check if port is available (optional check)
if command -v lsof >/dev/null 2>&1; then
    if lsof -Pi :${JUPYTER_PORT} -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo "[WARN] Port ${JUPYTER_PORT} appears to be in use." >&2
        echo "[WARN] Jupyter may fail to start or you may need to use a different port." >&2
        echo "[WARN] Set JUPYTER_PORT environment variable to use a different port." >&2
        echo ""
    fi
fi

# Start Jupyter Lab
echo "[INFO] Starting Jupyter Lab from local virtual environment..."
echo "[INFO] Virtual environment: ${VENV_DIR}"
echo "[INFO] Port: ${JUPYTER_PORT}"
echo "[INFO] Jupyter will be available at: http://localhost:${JUPYTER_PORT}"
echo "[INFO] To use a different port, set JUPYTER_PORT environment variable"
echo ""
exec jupyter lab --ip=127.0.0.1 --port=${JUPYTER_PORT} --no-browser

