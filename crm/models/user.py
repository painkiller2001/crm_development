
from sqlalchemy import Column, Integer, String
from crm.core.database import Base


class User(Base):
    __tablename__ = 'users'


    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    department = Column(String, nullable=False)

    def get_username(self):
        return f'{self.first_name}_{self.last_name}'