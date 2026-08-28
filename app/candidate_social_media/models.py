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





class candidate_social_media(Base):
    __tablename__ = "social_media"

    users_id: Mapped[int] = mapped_column(Integer(100), primary_key=True, index=True)
    candidate_id: Mapped[int] = mapped_column(ForeignKey("candidate.id"))
    facebook_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    twitter_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    linkedin_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    youtube_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    instagram_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    add_social_media_link: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    previous: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    save_and_next: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)


    #relationship

    
    candidate_social_media: Mapped [List["candidate_social_media"]] = relationship(back_populates="users")