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
 
class contact(Base):
    __tablename__ = "contacts"
    address: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)

    
    #relationships
    employer: Mapped["employer_profile"] = relationship(back_populates="contact")