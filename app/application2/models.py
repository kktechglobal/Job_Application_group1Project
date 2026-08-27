from datetime import datetime

import string

from typing import Optional, TYPE_CHECKING

from sqlalchemy import primarykey, ForeignKey, Float, Text,func,nullable,ApplicationStatus
from sqlalchemy import String, Integer, Boolean, DateTime,str
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.job_post.models import job_posts
    from app.candidate_profile.models import candidate_profiles
    from app.interview.models import interview
    





class Application2(Base):
    __tablename__ = "applications"

    id:Mapped[int] = mapped_column(Integer(100),primary_key=True)
    job_id: Mapped[int] = mapped_column(ForeignKey("job_posts.id"))
    add_new_column:Mapped[str] = mapped_column(string, nullable=True)
    add_column: Mapped[str] = mapped_column(string)
    column_name:Mapped[str] = mapped_column(string)
    cancel:Mapped [str] = mapped_column (string)

    #relationship
    Application2: Mapped[Application2] = relationship(back_populates="application")