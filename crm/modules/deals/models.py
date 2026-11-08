from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column

from crm.core.database import Base


class DealModel(Base):

    __tablename__ = 'deals'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'), nullable=False)  # -> ENUM
    responsible_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False) # -> FK users,  ENUM
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    stage: Mapped[str] = mapped_column(nullable=False) # -> ENUM
    description: Mapped[str | None] = mapped_column(nullable=True)