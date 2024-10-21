import importlib
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for filename in os.listdir(os.path.join('team_builder_api', 'app', 'api')):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = f"team_builder_api.app.api.{filename[:-3]}"
        module = importlib.import_module(module_name)

        if hasattr(module, "router"):
            app.include_router(module.router, prefix="/api", tags=[filename[:-3].replace('_', '-')])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}