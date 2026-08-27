from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import primarykey, ForeignKey, Float, Text,func,  nullable 
from sqlalchemy import String, Integer, Boolean, DateTime,bool
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.application.models import users
    from app.application.models import candidate_profile
    from app.application.models import application
 
class settings(Base):
    __tablename__ = "account_information"

    user_id: Mapped [int] = mapped_column(Integer(100),primary_key=True)
    application_id: Mapped[int]= mapped_column(Integer(100),ForeignKey(primarykey)) 

    address: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)


    change_password: Mapped[int] = mapped_column(String(100),nullable=True)
    current_password: Mapped[int] = mapped_column(String(100),nullable=True)
    new_password: Mapped[int] = mapped_column(String(100),nullable=True)

    #relationshiop
    candidate_profile: Mapped["candidate_profile"] = relationship( back_populates="candidate_profile")
    users:Mapped["users"] = relationship( back_populates="user")

       