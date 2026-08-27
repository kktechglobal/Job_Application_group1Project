from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import primarykey, ForeignKey, Float, Text,func,  nullable 
from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.application.models import users
    from app.application.models import employer_profile
    from app.application.models import application
 
class JobPost(Base):
    __tablename__ = "job_posts"

    id: Mapped[int] = mapped_column(Integer(100), primary_key=True, index=True)
    employer_id: Mapped[int] = mapped_column(ForeignKey("employer_profiles.id"))
    title: Mapped[str] = mapped_column(String(200), index=True, nullable=False)
    tag: Mapped[str] = mapped_column(String(200), index=True, nullable=False)
    job_role: Mapped[str] = mapped_column(String(200), index=True, nullable=False)
    job_description: Mapped[str] = mapped_column(Text, nullable=False)
    location: Mapped[str] = mapped_column(String(200), index=True, nullable=False)
    salary_min: Mapped[float] = mapped_column(Float, nullable=False)
    salary_max: Mapped[float] = mapped_column(Float, nullable=False)
    salary_type: Mapped[str] = mapped_column(String(200), nullable=False)
    vacancies: Mapped[int] = mapped_column(Integer, nullable=False)
    expiration_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    job_level: Mapped[str] = mapped_column(String(200), nullable=False)
    experience_level: Mapped[str] = mapped_column(String(200), nullable=False)
    job_type: Mapped[str] = mapped_column(String(200), nullable=False)
    fully_remote: Mapped[str] = mapped_column(Boolean, default=False, index=True)
    country: Mapped[str] = mapped_column(String(200), nullable=False)
    city: Mapped[str] = mapped_column(String(200), nullable=False)
    required_skills: Mapped[str] = mapped_column((String(200)), nullable= False)
    job_benefits: Mapped[str] = mapped_column((String(200)), nullable= False)
    subscription_plan: Mapped[str] = mapped_column(String(200), nullable=False)
    is_published: Mapped[bool] = mapped_column(Boolean, default=False)
    is_approved_by_admin: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime)



    #relatioship

    employer: Mapped["employer_profile"] = relationship(back_populates="jobs")
    applications: Mapped[List["application"]] = relationship( back_populates="job")