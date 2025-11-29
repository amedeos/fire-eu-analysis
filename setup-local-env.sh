#!/usr/bin/env bash
# Setup script for local Python virtual environment
# This creates a venv without CUDA dependencies for local Jupyter development

set -euo pipefail

VENV_DIR="${VENV_DIR:-venv}"

echo "[INFO] Setting up local Python virtual environment..."

# Function to find available Python versions
find_python_versions() {
    local versions=()
    local commands=()
    
    # Check common Python commands (minimum version 3.11)
    for cmd in python3.14 python3.13 python3.12 python3.11 python3; do
        if command -v "$cmd" >/dev/null 2>&1; then
            local version=$($cmd --version 2>&1 | cut -d' ' -f2)
            local major_minor=$(echo "$version" | cut -d'.' -f1,2)
            
            # Check if version is 3.11 or higher
            if [ "$(printf '%s\n' "3.11" "$major_minor" | sort -V | head -n1)" = "3.11" ]; then
                versions+=("$version ($cmd)")
                commands+=("$cmd")
            fi
        fi
    done
    
    # Return via global arrays (bash limitation)
    PYTHON_VERSIONS=("${versions[@]}")
    PYTHON_COMMANDS=("${commands[@]}")
}

# Find available Python versions
find_python_versions

# Check if any Python versions were found
if [ ${#PYTHON_COMMANDS[@]} -eq 0 ]; then
    echo "[ERROR] No suitable Python version (3.11+) found." >&2
    echo "Please install Python 3.11 or higher." >&2
    exit 1
fi

# If PYTHON_CMD is set via environment variable, use it
if [ -n "${PYTHON_CMD:-}" ]; then
    if command -v "${PYTHON_CMD}" >/dev/null 2>&1; then
        SELECTED_CMD="${PYTHON_CMD}"
        echo "[INFO] Using Python from PYTHON_CMD: ${PYTHON_CMD}"
    else
        echo "[WARN] PYTHON_CMD='${PYTHON_CMD}' not found. Showing selection menu..." >&2
        PYTHON_CMD=""
    fi
fi

# If not set, show selection menu
if [ -z "${PYTHON_CMD:-}" ]; then
    echo ""
    echo "Available Python versions:"
    for i in "${!PYTHON_VERSIONS[@]}"; do
        echo "  $((i+1))) ${PYTHON_VERSIONS[$i]}"
    done
    echo ""
    
    # Default to first option if only one is available
    if [ ${#PYTHON_COMMANDS[@]} -eq 1 ]; then
        SELECTED_CMD="${PYTHON_COMMANDS[0]}"
        echo "[INFO] Only one Python version found. Using: ${SELECTED_CMD}"
    else
        # Prompt user for selection
        while true; do
            read -p "Select Python version (1-${#PYTHON_COMMANDS[@]}): " selection
            if [[ "$selection" =~ ^[0-9]+$ ]] && [ "$selection" -ge 1 ] && [ "$selection" -le ${#PYTHON_COMMANDS[@]} ]; then
                SELECTED_CMD="${PYTHON_COMMANDS[$((selection-1))]}"
                break
            else
                echo "[ERROR] Invalid selection. Please enter a number between 1 and ${#PYTHON_COMMANDS[@]}." >&2
            fi
        done
    fi
fi

# Verify selected Python command
PYTHON_CMD="${SELECTED_CMD}"
PYTHON_VERSION=$(${PYTHON_CMD} --version | cut -d' ' -f2)
PYTHON_MAJOR_MINOR=$(echo "$PYTHON_VERSION" | cut -d'.' -f1,2)

# Final check: ensure version is 3.11 or higher
if [ "$(printf '%s\n' "3.11" "$PYTHON_MAJOR_MINOR" | sort -V | head -n1)" != "3.11" ]; then
    echo "[ERROR] Python 3.11 or higher is required. Selected version: ${PYTHON_VERSION}" >&2
    exit 1
fi

echo "[INFO] Selected Python: ${PYTHON_CMD} (version ${PYTHON_VERSION})"

# Create virtual environment if it doesn't exist
if [ -d "${VENV_DIR}" ]; then
    echo "[WARN] Virtual environment '${VENV_DIR}' already exists."
    read -p "Do you want to recreate it? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "[INFO] Removing existing virtual environment..."
        rm -rf "${VENV_DIR}"
    else
        echo "[INFO] Using existing virtual environment."
    fi
fi

if [ ! -d "${VENV_DIR}" ]; then
    echo "[INFO] Creating virtual environment in '${VENV_DIR}'..."
    ${PYTHON_CMD} -m venv "${VENV_DIR}"
fi

# Activate virtual environment
echo "[INFO] Activating virtual environment..."
source "${VENV_DIR}/bin/activate"

# Upgrade pip
echo "[INFO] Upgrading pip..."
pip install --upgrade pip --quiet

# Install requirements
echo "[INFO] Installing Python dependencies..."
echo "[INFO] Note: PyTorch will be installed in CPU-only mode (no CUDA required)"
pip install --no-cache-dir -r requirements.txt

echo ""
echo "[SUCCESS] Local environment setup complete!"
echo ""
echo "Python version used: ${PYTHON_VERSION}"
echo "Virtual environment: ${VENV_DIR}"
echo ""
echo "To activate the virtual environment, run:"
echo "  source ${VENV_DIR}/bin/activate"
echo ""
echo "To start Jupyter Lab locally, run:"
echo "  jupyter lab"
echo ""
echo "Or use the helper script:"
echo "  ./start-local-jupyter.sh"
echo ""

