from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from crm.core.database import Base


class CustomerModel(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    website = Column(String, nullable=True)
    address = Column(String, nullable=False)
    # responsible = ... # -> FK users