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
 
class my_job(Base):
    __tablename__ = "my_job"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    employer_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("employer_profile.id"), nullable=True)
    job_post_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("job_post.id"), nullable=True)
    job: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    total_jobs:Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    status: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    active: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    expires_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    applications: Mapped[Optional[List["application"]]] = relationship("application", back_populates="my_job")
    num_applicants: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    action: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    view_applications: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    promote_job: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    view_details: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    make_it_expire: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)

    next_page: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)


    #relationships
    employer: Mapped["employer_profile"] = relationship("employer_profile", foreign_keys=[employer_id])