from sqlalchemy.orm import Session
from app import models


def create_candidate(db: Session, data, resume_filename):
    candidate = models.Candidate(
        full_name=data.full_name,
        dob=data.dob,
        contact_number=data.contact_number,
        contact_address=data.contact_address,
        education=data.education,
        graduation_year=data.graduation_year,
        years_of_experience=data.years_of_experience,
        skill_set=data.skill_set,
        resume_file=resume_filename
    )

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return candidate


def get_candidates(db: Session, skill=None, experience=None, graduation_year=None):

    query = db.query(models.Candidate)

    if skill:
        query = query.filter(models.Candidate.skill_set.contains(skill))

    if experience:
        query = query.filter(models.Candidate.years_of_experience >= experience)

    if graduation_year:
        query = query.filter(models.Candidate.graduation_year == graduation_year)

    return query.all()


def get_candidate_by_id(db: Session, candidate_id: int):

    return db.query(models.Candidate).filter(
        models.Candidate.id == candidate_id
    ).first()


def delete_candidate(db: Session, candidate_id: int):

    candidate = db.query(models.Candidate).filter(
        models.Candidate.id == candidate_id
    ).first()

    if candidate:
        db.delete(candidate)
        db.commit()

    return candidate