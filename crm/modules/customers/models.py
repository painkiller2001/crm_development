from sqlalchemy.orm import Mapped, mapped_column

from crm.core.database import Base


class CustomerModel(Base):
    
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    website: Mapped[str] = mapped_column(nullable=True)
    address: Mapped[str] = mapped_column(nullable=False)
    # responsible = ... # -> FK users