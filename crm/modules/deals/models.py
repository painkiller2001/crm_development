from sqlalchemy import Column, Integer, String, DateTime, func
from crm.core.database import Base


class Deal(Base):

    __tablename__ = 'deals'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    customer = Column(String, nullable=False) # -> FK
    responsible = Column(String, nullable=False) # -> FK
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    price = Column(Integer, nullable=False)
    stage = Column(String, nullable=False) # -> FK
    description = Column(String, nullable=True)