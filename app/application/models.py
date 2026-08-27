from datetime import datetime

import string
from typing import Optional, TYPE_CHECKING

from sqlalchemy import primarykey, ForeignKey, Float, Text,func,nullable,ApplicationStatus
from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.job_post.models import job_posts
    from app.candidate_profile.models import candidate_profiles
    from app.interview.models import interview
    





class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    job_id: Mapped[int] = mapped_column(ForeignKey("job_posts.id"))
    candidate_id: Mapped[int] = mapped_column(ForeignKey("candidate_profiles.id"))

    job_application:Mapped[str] = mapped_column(String(255), nullable=True)

    notification_id: Mapped[Optional[int]] = mapped_column(ForeignKey("notifications.id"), nullable=True)
    edit_job_application: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    delete_job_application: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)

    filter_applications: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    sort_applications: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    newest: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    oldest: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)  
    
    status: Mapped[ApplicationStatus] = mapped_column(default=ApplicationStatus.SUBMITTED)
    cover_letter: Mapped[Optional[str]] = mapped_column(Text)
    match_score: Mapped[float] = mapped_column(Float, default=0.0)
    submitted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    job: Mapped["job_posts"] = relationship(back_populates="applications")
    candidate: Mapped["candidate_profiles"] = relationship(back_populates="applications")
    interview: Mapped["interview"] = relationship(back_populates="application")
    job_application: Mapped[Optional["job_posts"]] = relationship( back_populates="applications")