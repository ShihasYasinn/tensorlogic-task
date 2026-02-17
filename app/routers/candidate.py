import os
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas, models

router = APIRouter(prefix="/candidates", tags=["Candidates"])

UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
async def create_candidate(
    full_name: str = Form(..., example=""),
    dob: str = Form(..., example=""),
    contact_number: str = Form(..., example=""),
    contact_address: str = Form(..., example=""),
    education: str = Form(..., example=""),
    graduation_year: int = Form(..., example=""),
    years_of_experience: float = Form(..., example=""),
    skill_set: str = Form(..., example=""),
    resume: UploadFile = File(..., description="Upload PDF/DOC/DOCX file"),
    db: Session = Depends(get_db)
):

    file_path = os.path.join(UPLOAD_DIR, resume.filename)

    with open(file_path, "wb") as f:
        f.write(await resume.read())

    data = schemas.CandidateBase(
        full_name=full_name,
        dob=dob,
        contact_number=contact_number,
        contact_address=contact_address,
        education=education,
        graduation_year=graduation_year,
        years_of_experience=years_of_experience,
        skill_set=skill_set
    )

    return crud.create_candidate(db, data, resume.filename)


@router.get("/")
def list_candidates(
    skill: str = None,
    experience: float = None,
    graduation_year: int = None,
    db: Session = Depends(get_db)
):
    return crud.get_candidates(db, skill, experience, graduation_year)


@router.get("/{candidate_id}")
def get_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = crud.get_candidate_by_id(db, candidate_id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return candidate


@router.delete("/{candidate_id}")
def delete_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = crud.delete_candidate(db, candidate_id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return {"message": "Deleted successfully"}
