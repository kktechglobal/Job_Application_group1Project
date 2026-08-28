from datetime import datetime
import string
from typing import Optional, TYPE_CHECKING

from sqlalchemy import primarykey, ForeignKey, Float, Text,func,  nullable 
from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.application.models import users
    from app.application.models import application



class Interview(Base):
    __tablename__ = "interviews"

    id: Mapped[int] = mapped_column(Integer(100), primary_key=True, index=True)
    application_id: Mapped[int] = mapped_column(ForeignKey("applications.id"), unique=True)
    scheduled_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    meeting_link: Mapped[str] = mapped_column(String(200), nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)


    #relationship

    application: Mapped["application"] = relationship(back_populates="interview")