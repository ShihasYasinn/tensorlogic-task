from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import candidate

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mini Resume Management API",
    description="""
    ## Resume Management System
    
    A lightweight API for managing candidate resumes and profiles.
    
     Features:
    * Create Candidates - Add new candidate profiles with resume uploads
    * List Candidates - Retrieve all candidates with their information
    * Get Candidate - Fetch specific candidate details by ID
    * Delete Candidate - Remove candidate records from the system
    
     Tech Stack:
    * FastAPI for high-performance REST API
    * SQLAlchemy ORM for database operations
    * SQLite for data persistence
    * Pydantic for data validation
    
     How it Works:
    1. Upload candidate information via POST endpoint
    2. Store resume files in the uploads directory
    3. Manage candidate data through CRUD operations
    4. Retrieve and filter candidates as needed
    """,
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@example.com",
    },
    license_info={
        "name": "MIT",
    }
)

app.include_router(candidate.router)
