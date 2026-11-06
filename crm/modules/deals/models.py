from sqlalchemy import Column, Integer, DateTime, func
from crm.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Deal(Base):

    __tablename__ = 'deals'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    customer: Mapped[str] = mapped_column(nullable=False) # -> FK customer
    responsible: Mapped[str] = mapped_column(nullable=False) # -> FK users
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    stage: Mapped[str] = mapped_column(nullable=False) # -> ENUM
    description: Mapped[str] = mapped_column(nullable=True)