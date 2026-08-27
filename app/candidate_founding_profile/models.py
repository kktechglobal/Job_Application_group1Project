from datetime import datetime

import string
from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import primarykey, ForeignKey, Float, Text,func,  nullable 
from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.application.models import users
    from app.employer_profile.models import employer_profile
    from app.application.models import application
    from app.employer_profile.models import job_post





class CandidateProfile(Base):
    __tablename__ = "candidate_profiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)


    organization_type: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    year_of_establishment: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    industry_type: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    team_size: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    company_website: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    company_vision: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    


    # headline: Mapped[Optional[str]] = mapped_column(String(200))
    # resume_url: Mapped[Optional[str]] = mapped_column(String(200))

    # skills: Mapped[List[str]] = mapped_column((String(200)  ), default=[])
    # years_experience: Mapped[int] = mapped_column(Integer, default=0)

    # completeness_score: Mapped[int] = mapped_column(Integer, default=0)

    #relatioship
    user: Mapped["users"] = relationship("User", back_populates="profile")
    applications: Mapped [List["application"]] = relationship(back_populates="candidate")