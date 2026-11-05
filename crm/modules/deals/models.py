from sqlalchemy import Column, Integer, String, Time
from crm.core.database import Base


class Deal(Base):

    __tablename__ = 'deals'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    customer = Column(String)
    responsible = Column(String)
    created_at = Column(Time)
    price = Column(Integer)
    stage = Column(String)
    description = Column(String)