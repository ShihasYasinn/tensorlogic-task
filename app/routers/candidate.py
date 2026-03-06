import os
from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app import crud, schemas

router = APIRouter(prefix="/candidates", tags=["Candidates"])

UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.CandidateResponse)
async def create_candidate(
    full_name: str = Form(...),
    dob: str = Form(...),
    contact_number: str = Form(...),
    contact_address: str = Form(...),
    education: str = Form(...),
    graduation_year: int = Form(...),
    years_of_experience: float = Form(...),
    skill_set: str = Form(...),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = os.path.join(UPLOAD_DIR, resume.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await resume.read())

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

    candidate = crud.create_candidate(db, data, resume.filename)

    response = schemas.CandidateResponse.model_validate(candidate)
    response.resume_url = f"/uploads/{candidate.resume_file}"

    return response


@router.get("/", response_model=List[schemas.CandidateResponse])
def list_candidates(
    skill: str = None,
    experience: float = None,
    graduation_year: int = None,
    db: Session = Depends(get_db)
):

    candidates = crud.get_candidates(db, skill, experience, graduation_year)

    response = []
    for candidate in candidates:
        item = schemas.CandidateResponse.model_validate(candidate)
        item.resume_url = f"/uploads/{candidate.resume_file}"
        response.append(item)

    return response


@router.get("/{candidate_id}", response_model=schemas.CandidateResponse)
def get_candidate(candidate_id: int, db: Session = Depends(get_db)):

    candidate = crud.get_candidate_by_id(db, candidate_id)

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    response = schemas.CandidateResponse.model_validate(candidate)
    response.resume_url = f"/uploads/{candidate.resume_file}"

    return response


@router.delete("/{candidate_id}")
def delete_candidate(candidate_id: int, db: Session = Depends(get_db)):

    candidate = crud.delete_candidate(db, candidate_id)

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return {"message": "Deleted successfully"}