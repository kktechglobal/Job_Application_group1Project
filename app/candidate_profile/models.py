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
    headline: Mapped[Optional[str]] = mapped_column(String)
    resume_url: Mapped[Optional[str]] = mapped_column(String)
    skills: Mapped[List[str]] = mapped_column((String), default=[])
    years_experience: Mapped[int] = mapped_column(Integer, default=0)
    completeness_score: Mapped[int] = mapped_column(Integer, default=0)

    user: Mapped["users"] = relationship("User", back_populates="profile")
    applications: Mapped [List["application"]] = relationship(back_populates="candidate")