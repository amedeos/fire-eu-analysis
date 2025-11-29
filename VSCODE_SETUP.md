# VS Code Setup for Jupyter in Container

This guide explains how to use VS Code to develop and execute Jupyter notebooks in the Docker container.

## Initial Setup

### 1. Start the container

```bash
./fire.sh start --build
```

The container will automatically start Jupyter Lab and generate an authentication token.

### 2. Get the Jupyter token

```bash
./get-jupyter-token.sh
```

Copy the displayed token. Or read the file directly:

```bash
cat .jupyter_token
```

### 3. Configure VS Code

#### Option A: Direct connection to Jupyter server (Recommended)

1. Open a `.ipynb` notebook in VS Code
2. Click on the kernel selector (top right in the notebook)
3. Select "Existing Jupyter Server"
4. Enter the URL: `http://localhost:8888`
5. Enter the token obtained in step 2
6. Click "Connect"

#### Option B: Automatic configuration

The `.vscode/settings.json` file is already configured. You just need to:

1. Open a notebook in VS Code
2. Select the "Fire EU Analysis Container" kernel when prompted
3. If needed, update the token in `.vscode/settings.json` with the one obtained from `./get-jupyter-token.sh`

## Development Workflow

### Development in VS Code

1. **Create/modify notebooks** directly in VS Code
2. **Execute cells** using the remote kernel in the container
3. **Files are automatically synchronized** thanks to the volume mount

### Benefits

- ✅ Development with autocompletion and IntelliSense in VS Code
- ✅ Execution in container with all dependencies
- ✅ Automatic file synchronization
- ✅ Integrated debug and profiling
- ✅ Native Git integration

## Troubleshooting

### Token doesn't work

If the token is not recognized:

1. Restart the container: `./fire.sh stop && ./fire.sh start`
2. Get the new token: `./get-jupyter-token.sh`
3. Update the configuration in VS Code

### VS Code doesn't connect to server

Verify that:
- The container is running: `podman ps | grep fire-eu-analysis`
- Jupyter is accessible: open `http://localhost:8888` in browser
- Port 8888 is not blocked by firewall

### Kernel not available

If the kernel doesn't appear:

1. Verify that Jupyter Lab is started in the container:
   ```bash
   podman exec fire-eu-analysis jupyter lab list
   ```
2. Restart the container if necessary

## Alternative: Jupyter Lab in Browser

If you prefer to use Jupyter Lab directly in the browser:

1. Start the container: `./fire.sh start`
2. Open `http://localhost:8888` in browser
3. Enter the token (if requested): `./get-jupyter-token.sh`
4. Develop notebooks in the browser

Notebooks created in the browser will also be visible in VS Code thanks to the volume mount.

## Notes

- The token is regenerated on each container startup
- Notebooks are saved in the project directory (synchronized with host)
- All Python dependencies are available in the container
- For GPU, use: `./fire.sh start --gpu`

## Alternative: Local Virtual Environment

If you prefer to run Jupyter locally without Docker, you can set up a Python virtual environment:

### Setup Local Environment

1. **Create and activate virtual environment:**
   ```bash
   ./setup-local-env.sh
   ```

   This will:
   - Create a Python virtual environment in `venv/`
   - Install all dependencies from `requirements.txt`
   - Install PyTorch in CPU-only mode (no CUDA required)

2. **Start Jupyter Lab locally:**
   ```bash
   ./start-local-jupyter.sh
   ```

   By default, local Jupyter uses port **8889** (to avoid conflict with container on 8888).
   
   To use a different port:
   ```bash
   JUPYTER_PORT=8890 ./start-local-jupyter.sh
   ```

   Or manually:
   ```bash
   source venv/bin/activate
   jupyter lab --port=8889
   ```

### Local Environment Benefits

- ✅ No Docker/Podman required
- ✅ Faster startup time
- ✅ Direct access to local filesystem
- ✅ No CUDA needed (PyTorch CPU-only)
- ✅ Same dependencies as container

### When to Use Local vs Container

**Use Local Environment when:**
- You don't need GPU acceleration
- You want faster iteration
- You prefer not to use containers
- You're working on a machine without Docker/Podman

**Use Container when:**
- You need GPU support (CUDA)
- You want environment isolation
- You need reproducible deployments
- You're working across different machines

### VS Code with Local Environment

To use the local virtual environment in VS Code:

**Option 1: Use local Python interpreter (Recommended)**
1. Open a notebook in VS Code
2. Click on the kernel selector (top right)
3. Select "Python Environments"
4. Choose the interpreter from `venv/bin/python`

Or configure it in `.vscode/settings.json`:
```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python"
}
```

**Option 2: Connect to local Jupyter server**
1. Start local Jupyter: `./start-local-jupyter.sh` (runs on port 8889 by default)
2. Open a notebook in VS Code
3. Click on the kernel selector (top right)
4. Select "Existing Jupyter Server"
5. Enter URL: `http://localhost:8889` (or the port you specified)
6. Leave token empty (local server doesn't require token by default)

