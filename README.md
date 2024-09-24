# Team Builder API
## Overview
The team Builder API is built with FastAPI and Poetry (Python 3.12). In order to run this project, you will need to install [poetry](https://python-poetry.org/docs/)

## Setting up
1. Install Poetry: [Poetry Documentation](https://python-poetry.org/docs/)
2. Run ```poetry install``` to install dependencies.
3. Run ```poetry run dev``` to start up a development server. You can access it at http://localhost:8000 in your web browser.

## Development
### Creating Routes
When devleoping, use ```poetry run dev``` which will start a server with hot reloading. To make a new endpoint, create a new file inside the ```team_builder_api/app/api``` following the same format as existing files.

### Utility Functions
Utility functions are simple and reusable. These will be things like getting our S3 Client or handling authentication. These will be inside ```team_builder_api/app/utils```.

### Library Functions
Library functions will be where a lot of our main logic will be stored. Our routes will mostly be calling these library functions from the ```team_builder_api/app/lib``` directory.