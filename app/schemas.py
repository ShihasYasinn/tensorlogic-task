from pydantic import BaseModel

class CandidateBase(BaseModel):
    full_name: str
    dob: str
    contact_number: str
    contact_address: str
    education: str
    graduation_year: int
    years_of_experience: float
    skill_set: str

class CandidateResponse(CandidateBase):
    id: int
    resume_file: str

    class Config:
        orm_mode = True
