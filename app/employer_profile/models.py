from datetime import datetime

import string
from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import primarykey, ForeignKey, Float, Text,func,  nullable 
from sqlalchemy import String, Integer, Boolean, DateTime,list
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.users.models import user
    from app.employer_profile.models import employer_profile
    from app.employer_profile.models import application
    from app.employer_profile.models import job_post




class employer_Profile(Base):
    __tablename__ = "employer_profiles"

    id: Mapped[int] = mapped_column(Integer(100), primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)

    company_name: Mapped[str] = mapped_column(String(200), nullable=False)
    company_description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    about: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    banner_image_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    logo_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)

    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    
    save_and_next: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)


    #relationship
    user: Mapped["user"] = relationship( back_populates="employer_profile")
    jobs: Mapped[list["job_post"]] = relationship( back_populates="employer")



