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
 
class company_socialmedia(Base):
    __tablename__ = "company_socialmedia"

    id: Mapped[int] = mapped_column(Integer(100), primary_key=True, index=True)
    employer_id: Mapped[int] = mapped_column(ForeignKey("employer_profiles.id"))
    facebook_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    twitter_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    linkedin_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    youtube_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    instagram_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    add_social_media_link: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    

    #relationships
    employer: Mapped["employer_profile"] = relationship(back_populates="company_socialmedia")
    user: Mapped["users"] = relationship(back_populates="company_socialmedia")