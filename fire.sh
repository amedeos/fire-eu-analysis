#!/usr/bin/env bash
set -euo pipefail

# -------------------------------------------------------------------
# Configuration
# -------------------------------------------------------------------
PODMAN_BIN="podman"

CPU_IMAGE="fire-eu-analysis:dev"
GPU_IMAGE="fire-eu-analysis:gpu"

# Default container name (override with --name)
CONTAINER_NAME="fire-eu-analysis"

# Mode: auto | gpu | cpu
# Can be overridden by env START_MODE or CLI flags
MODE="${START_MODE:-auto}"

# Build flag: if true, build images before starting
BUILD_IMAGES=false

# Remove images flag: if true, remove images when removing container
REMOVE_IMAGES=false

# Command: start (default) | stop | remove
COMMAND="start"

# -------------------------------------------------------------------
# Functions
# -------------------------------------------------------------------

usage() {
  cat <<EOF
Usage: $0 [COMMAND] [OPTIONS]

Commands:
  start       Start the container (default)
  stop        Stop the running container
  remove      Remove the container (use --remove-image to also remove images)

Options for 'start':
  --auto       Automatically choose GPU if available, otherwise CPU (default)
  --gpu        Force GPU container
  --cpu        Force CPU container
  --name NAME  Set container name (default: ${CONTAINER_NAME})
  --build      Build images before starting (auto-detects GPU/CUDA for Dockerfile selection)

Options for 'remove':
  --remove-image  Also remove the container images (CPU and/or GPU)

Global options:
  --name NAME  Set container name (default: ${CONTAINER_NAME})
  -h, --help   Show this help

Environment:
  START_MODE   Can be set to auto, gpu, or cpu (overridden by CLI flags)

Examples:
  $0 start                    # Start container (auto-detect GPU)
  $0 start --gpu --build      # Start GPU container, build images first
  $0 stop                     # Stop the container
  $0 remove                   # Remove the container
  $0 remove --remove-image    # Remove container and images
EOF
}

has_gpu() {
  if command -v nvidia-smi >/dev/null 2>&1; then
    if nvidia-smi -q >/dev/null 2>&1; then
      return 0
    fi
  fi
  return 1
}

has_cuda() {
  # Check if CUDA is available (nvidia-smi or CUDA libraries)
  if has_gpu; then
    return 0
  fi
  # Also check for CUDA libraries in common paths
  if [ -d "/usr/local/cuda" ] || [ -d "/opt/cuda" ]; then
    return 0
  fi
  return 1
}

image_exists() {
  local image_name="$1"
  ${PODMAN_BIN} image exists "${image_name}" >/dev/null 2>&1
}

build_cpu_image() {
  echo "[INFO] Building CPU image '${CPU_IMAGE}' using Dockerfile..."
  ${PODMAN_BIN} build -f Dockerfile -t "${CPU_IMAGE}" .
  if [ $? -eq 0 ]; then
    echo "[INFO] CPU image '${CPU_IMAGE}' built successfully"
  else
    echo "[ERROR] Failed to build CPU image" >&2
    return 1
  fi
}

build_gpu_image() {
  echo "[INFO] Building GPU image '${GPU_IMAGE}' using Dockerfile.gpu..."
  ${PODMAN_BIN} build -f Dockerfile.gpu -t "${GPU_IMAGE}" .
  if [ $? -eq 0 ]; then
    echo "[INFO] GPU image '${GPU_IMAGE}' built successfully"
  else
    echo "[ERROR] Failed to build GPU image" >&2
    return 1
  fi
}

build_images() {
  echo "[INFO] Building images based on GPU/CUDA availability..."
  
  if has_cuda; then
    echo "[INFO] CUDA/GPU detected. Building both CPU and GPU images..."
    build_cpu_image || return 1
    build_gpu_image || return 1
  else
    echo "[INFO] No CUDA/GPU detected. Building CPU image only..."
    build_cpu_image || return 1
  fi
  
  echo "[INFO] Image build completed"
}

container_exists() {
  ${PODMAN_BIN} ps -a --format '{{.Names}}' | grep -qx "$CONTAINER_NAME" || return 1
}

container_running() {
  ${PODMAN_BIN} ps --format '{{.Names}}' | grep -qx "$CONTAINER_NAME" || return 1
}

stop_container() {
  if ! container_exists; then
    echo "[WARN] Container '${CONTAINER_NAME}' does not exist."
    return 0
  fi

  if ! container_running; then
    echo "[INFO] Container '${CONTAINER_NAME}' is not running."
    return 0
  fi

  echo "[INFO] Stopping container '${CONTAINER_NAME}'..."
  ${PODMAN_BIN} stop "${CONTAINER_NAME}" >/dev/null
  echo "[INFO] Container '${CONTAINER_NAME}' stopped."
}

remove_container() {
  if ! container_exists; then
    echo "[WARN] Container '${CONTAINER_NAME}' does not exist."
  else
    if container_running; then
      echo "[INFO] Container '${CONTAINER_NAME}' is running. Stopping it first..."
      ${PODMAN_BIN} stop "${CONTAINER_NAME}" >/dev/null
    fi
    echo "[INFO] Removing container '${CONTAINER_NAME}'..."
    ${PODMAN_BIN} rm "${CONTAINER_NAME}" >/dev/null
    echo "[INFO] Container '${CONTAINER_NAME}' removed."
  fi

  if [[ "${REMOVE_IMAGES}" == "true" ]]; then
    echo "[INFO] Removing images..."
    if image_exists "${CPU_IMAGE}"; then
      echo "[INFO] Removing CPU image '${CPU_IMAGE}'..."
      ${PODMAN_BIN} rmi "${CPU_IMAGE}" || echo "[WARN] Failed to remove CPU image (may be in use)" >&2
    fi
    if image_exists "${GPU_IMAGE}"; then
      echo "[INFO] Removing GPU image '${GPU_IMAGE}'..."
      ${PODMAN_BIN} rmi "${GPU_IMAGE}" || echo "[WARN] Failed to remove GPU image (may be in use)" >&2
    fi
    echo "[INFO] Image removal completed."
  fi
}

start_gpu_container() {
  echo "[INFO] Starting GPU container '${CONTAINER_NAME}' using image '${GPU_IMAGE}'"
  ${PODMAN_BIN} run -d \
    --name "${CONTAINER_NAME}" \
    --userns=keep-id \
    --user "$(id -u):$(id -g)" \
    --group-add keep-groups \
    --device nvidia.com/gpu=all \
    -v "${PWD}:/workspace:Z" \
    -p 8888:8888 \
    "${GPU_IMAGE}"

  echo "[INFO] GPU container started. Jupyter should be available on http://localhost:8888"
}

start_cpu_container() {
  echo "[INFO] Starting CPU container '${CONTAINER_NAME}' using image '${CPU_IMAGE}'"
  ${PODMAN_BIN} run -d \
    --name "${CONTAINER_NAME}" \
    --userns=keep-id \
    --user "$(id -u):$(id -g)" \
    --group-add keep-groups \
    -v "${PWD}:/workspace:Z" \
    -p 8888:8888 \
    "${CPU_IMAGE}"

  echo "[INFO] CPU container started. Jupyter should be available on http://localhost:8888"
}

# -------------------------------------------------------------------
# CLI parsing
# -------------------------------------------------------------------

# Parse command (first argument if it's not a flag)
if [[ $# -gt 0 ]] && [[ ! "$1" =~ ^-- ]]; then
  COMMAND="$1"
  shift
fi

while [[ $# -gt 0 ]]; do
  case "$1" in
    --gpu)
      MODE="gpu"
      shift
      ;;
    --cpu)
      MODE="cpu"
      shift
      ;;
    --auto)
      MODE="auto"
      shift
      ;;
    --name)
      if [[ $# -lt 2 ]]; then
        echo "[ERROR] --name requires an argument" >&2
        exit 1
      fi
      CONTAINER_NAME="$2"
      shift 2
      ;;
    --build)
      BUILD_IMAGES=true
      shift
      ;;
    --remove-image)
      REMOVE_IMAGES=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "[ERROR] Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

# -------------------------------------------------------------------
# Safety checks
# -------------------------------------------------------------------

if ! command -v "${PODMAN_BIN}" >/dev/null 2>&1; then
  echo "[ERROR] podman not found. Please install Podman or adjust PODMAN_BIN." >&2
  exit 1
fi

# -------------------------------------------------------------------
# Execute command
# -------------------------------------------------------------------

case "${COMMAND}" in
  start)
    # Build images if requested
    if [[ "${BUILD_IMAGES}" == "true" ]]; then
      build_images || exit 1
    fi

    if container_running; then
      echo "[INFO] Container '${CONTAINER_NAME}' is already running."
      echo "[INFO] You can attach a shell with:"
      echo "       ${PODMAN_BIN} exec -it ${CONTAINER_NAME} bash"
      exit 0
    fi

    if container_exists; then
      echo "[WARN] Container '${CONTAINER_NAME}' exists but is not running."
      echo "[INFO] Starting existing container..."
      ${PODMAN_BIN} start "${CONTAINER_NAME}" >/dev/null
      echo "[INFO] Container started. Jupyter should be available on http://localhost:8888"
      exit 0
    fi

    # Mode resolution
    FINAL_MODE="${MODE}"

    if [[ "${MODE}" == "auto" ]]; then
      echo "[INFO] Auto mode: detecting GPU availability..."
      if has_gpu; then
        echo "[INFO] GPU detected via nvidia-smi. Using GPU container."
        FINAL_MODE="gpu"
      else
        echo "[INFO] No GPU detected. Falling back to CPU container."
        FINAL_MODE="cpu"
      fi
    fi

    # Check if images exist, build if missing
    case "${FINAL_MODE}" in
      gpu)
        if ! image_exists "${GPU_IMAGE}"; then
          echo "[INFO] GPU image '${GPU_IMAGE}' not found. Building it..."
          build_gpu_image || exit 1
        fi
        ;;
      cpu)
        if ! image_exists "${CPU_IMAGE}"; then
          echo "[INFO] CPU image '${CPU_IMAGE}' not found. Building it..."
          build_cpu_image || exit 1
        fi
        ;;
    esac

    # Start appropriate container
    case "${FINAL_MODE}" in
      gpu)
        start_gpu_container
        ;;
      cpu)
        start_cpu_container
        ;;
      *)
        echo "[ERROR] Invalid mode '${FINAL_MODE}'. Must be auto, gpu, or cpu." >&2
        exit 1
        ;;
    esac
    ;;
  stop)
    stop_container
    ;;
  remove)
    remove_container
    ;;
  *)
    echo "[ERROR] Unknown command '${COMMAND}'. Must be start, stop, or remove." >&2
    echo ""
    usage
    exit 1
    ;;
esac

