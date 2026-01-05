#!/bin/bash
# Start Jupyter Lab with token generation for remote access

# Generate a random token using Python
TOKEN=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))")

# Save token to file (accessible from host via volume mount)
echo "$TOKEN" > /workspace/.jupyter_token
echo "[Jupyter] Token saved to .jupyter_token: $TOKEN"

# Start Jupyter Lab
exec jupyter lab \
    --ip=0.0.0.0 \
    --no-browser \
    --ServerApp.token="$TOKEN" \
    --ServerApp.password='' \
    --ServerApp.allow_origin='*' \
    --ServerApp.disable_check_xsrf=True \
    --ServerApp.iopub_data_rate_limit=${JUPYTER_DATA_LIMIT:-100000000} \
    --ServerApp.iopub_msg_rate_limit=${JUPYTER_MSG_LIMIT:-100000}
