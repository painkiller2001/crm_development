from sqlalchemy import Columnt, Integer, String

from crm.core.database import Base


class CustomerModel(Base):
    __tablename__ = 'customers'

    ...