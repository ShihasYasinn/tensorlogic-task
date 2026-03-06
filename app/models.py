from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    dob = Column(String)
    contact_number = Column(String)
    contact_address = Column(String)
    education = Column(String)
    graduation_year = Column(Integer)
    years_of_experience = Column(Float)
    skill_set = Column(String)
    resume_file = Column(String)