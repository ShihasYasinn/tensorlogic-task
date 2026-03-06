# Mini Resume Management API

A REST API built using FastAPI for managing candidate resumes.

## Features

- Upload Resume (PDF/DOC/DOCX)
- Store Candidate Metadata
- Filter Candidates by:
  - Skill
  - Experience
  - Graduation Year
- Get Candidate by ID
- Delete Candidate

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

Database

The application uses SQLite for data persistence.

Candidate data including resume file names are stored
in the `resume.db` database using SQLAlchemy ORM.



## Setup Instructions

### 1. Clone Repository

git clone <your-repo-url>

cd resume_api

### 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run Server

uvicorn app.main:app --reload

Open:
http://127.0.0.1:8000/docs

---

## API Endpoints

POST /candidates/
GET /candidates/
GET /candidates/{id}
DELETE /candidates/{id}

---

