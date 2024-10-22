import subprocess
import sys

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

def migrate_up():
    try:
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        print("Migrated up to the latest version.")
    except KeyboardInterrupt:
        print("Migration stopped by user.")

def migrate_down(argv=sys.argv):
    n = len(argv)

    if (n != 2):
        print("Invalid arguments to migrate_down")
        return
    
    try:
        revision = argv[1]
        subprocess.run(["alembic", "downgrade", revision], check=True)
        print(f"Migration downgraded with revision: '{revision}'")
    except KeyboardInterrupt:
        print("Migration downgrade stopped by user.")

def migrate_create(argv=sys.argv):
    n = len(argv)

    if (n != 2):
        print("Invalid arguments to migrate_create")
        return
    
    try:
        message = argv[1]
        subprocess.run(["alembic", "revision", "-m", message], check=True)
        print(f"Migration created with message: '{message}'")
    except KeyboardInterrupt:
        print("Migration creation stopped by user.")