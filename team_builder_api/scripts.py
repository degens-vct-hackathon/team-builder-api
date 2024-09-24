import subprocess

def dev():
    """
    Starts the development server for the FastAPI application
    using Uvicorn with auto-reload enabled.
    
    Raises:
        subprocess.CalledProcessError: If the server fails to start.
    """
    try:
        subprocess.run(["uvicorn", "team_builder_api.app.main:app", "--reload"], check=True)
    except KeyboardInterrupt:
        print("Server stopped.")

def start():
    """
    Starts the development server for the FastAPI application
    using Uvicorn.
    
    Raises:
        subprocess.CalledProcessError: If the server fails to start.
    """
    try:
        subprocess.run(["uvicorn", "team_builder_api.app.main:app"], check=True)
    except KeyboardInterrupt:
        print("server Stopped")
