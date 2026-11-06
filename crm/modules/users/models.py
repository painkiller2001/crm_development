from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from crm.core.database import Base


class UserModel(Base):
    
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False) # -> ENUM
    department: Mapped[str] = mapped_column(nullable=False) # -> ENUM
    email: Mapped[str] = mapped_column(nullable=False, unique=True)

    def get_username(self):
        return f'{self.first_name}_{self.last_name}'