#!/usr/bin/env bash
# Helper script to get Jupyter token from running container

set -euo pipefail

PODMAN_BIN="${PODMAN_BIN:-podman}"
CONTAINER_NAME="${CONTAINER_NAME:-fire-eu-analysis}"

if ! ${PODMAN_BIN} ps --format '{{.Names}}' | grep -qx "$CONTAINER_NAME"; then
    echo "[ERROR] Container '$CONTAINER_NAME' is not running." >&2
    echo "Start it with: ./fire.sh start" >&2
    exit 1
fi

# Try to read token from file (if container has started Jupyter)
if ${PODMAN_BIN} exec "$CONTAINER_NAME" test -f /workspace/.jupyter_token 2>/dev/null; then
    TOKEN=$(${PODMAN_BIN} exec "$CONTAINER_NAME" cat /workspace/.jupyter_token 2>/dev/null | tr -d '\n\r ')
    if [ -n "$TOKEN" ]; then
        echo "$TOKEN"
        exit 0
    fi
fi

# Fallback: try to get token from Jupyter process
echo "[WARN] Token file not found. Trying to get token from Jupyter process..." >&2
${PODMAN_BIN} exec "$CONTAINER_NAME" jupyter lab list 2>/dev/null | grep -oP 'token=\K[^ ]+' | head -1 || {
    echo "[ERROR] Could not retrieve Jupyter token." >&2
    echo "Make sure Jupyter Lab is running in the container." >&2
    exit 1
}

