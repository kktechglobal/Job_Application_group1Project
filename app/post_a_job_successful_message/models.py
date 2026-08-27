from datetime import datetime
from typing import List,Optional, TYPE_CHECKING

from sqlalchemy import primarykey, ForeignKey, Float, Text,func,  nullable 
from sqlalchemy import String, Integer, Boolean, DateTime,bool
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.application.models import users
    from app.application.models import employer_profile
    from app.application.models import application
 
class post_a_job_successful_message(Base):
    __tablename__ = "post_a_job_successful_message"
    id: Mapped[int] = mapped_column(Integer(100), primary_key=True, index=True)
    employer_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("employer_profile.id"), nullable=True)
    view_job: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)

    
    feature_job: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    highlight_job: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)   
    promote_job: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)


    #relationships
    employer: Mapped["employer_profile"] = relationship("employer_profile", foreign_keys=[employer_id])