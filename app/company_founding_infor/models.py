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
 
class founding_info(Base):
    __tablename__ = "founding_info"

    id: Mapped[int] = mapped_column(Integer(100), primary_key=True, index=True)
    employer_id: Mapped[int] = mapped_column(ForeignKey("employer_profiles.id"))
    organization_type: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    year_of_establishment: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    industry_type: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    team_size: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    company_website: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    company_vision: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)

    


    #relationships
    employer: Mapped["employer_profile"] = relationship(back_populates="founding_info")