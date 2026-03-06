from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import engine
from app import models
from app.routers import candidate

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mini Resume Management API",
    description="API for managing candidate resumes",
    version="1.0.0"
)

app.mount("/uploads", StaticFiles(directory="app/uploads"), name="uploads")

app.include_router(candidate.router)