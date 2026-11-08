from pydantic import BaseModel, EmailStr


class DealBase(BaseModel):
    name: str
    customer_id: int #ENUM
    responsible_id: int #ENUM
    price: int
    stage: str # ENUM
    description: str | None = None


class DealCreate(DealBase):
    pass


class DealRead(DealBase):
    pass


class DealUpdate(BaseModel):
    name: str | None = None
    customer_id: int | None = None #ENUM
    responsible_id: int | None = None #ENUM
    price: int | None = None
    stage: str | None = None # ENUM
    description: str | None = None