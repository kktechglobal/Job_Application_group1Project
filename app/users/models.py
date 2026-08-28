from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlalchemy import String, Integer, Boolean, DateTime,primarykey, ForeignKey, Float, Text,func, Enum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.users.models import users
    from app.candidate_profile.models import candidate_profiles
    from app.employer_profile.models import employer_profiles
    
    


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer(100), primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(200), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(50), nullable=False)
    full_name: Mapped[str] = mapped_column(String(200), nullable=False)
    role: Mapped[str] = mapped_column(str(300), nulllable=False)  # 'candidate' or 'employer'
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


    # Relationships
    profile: Mapped["candidate_profiles"] = relationship(back_populates="user")
    employer_profile: Mapped["employer_profiles"] = relationship( back_populates="user")




   



