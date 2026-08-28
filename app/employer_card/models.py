from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import primarykey, ForeignKey, Float, Text,func,  nullable

from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app import candidate_profile
from app.database.base import Base
from app.employer_card import employer_id


if TYPE_CHECKING:
    from app.application.models import users
    from app.application.models import employer_profile
    from app.application.models import application
 
class card(Base):
    __tablename__ = "cards"
    id: Mapped[int] = mapped_column(Integer(100), primary_key=True, index=True)
    employer_id: Mapped[int] = mapped_column(ForeignKey("candidate_profiles.id"))

    #debit/credited_card
    cardholder_name: Mapped[str] = mapped_column(String(200), nullable=False)
    card_number: Mapped[str] = mapped_column(String(200), nullable=False)
    expiration_date: Mapped[str] = mapped_column(String(200), nullable=False)
    cvv: Mapped[str] = mapped_column(String(200), nullable=False)

    #relationships
    employer_card: Mapped["employer_id"] = relationship(back_populates="card")
    