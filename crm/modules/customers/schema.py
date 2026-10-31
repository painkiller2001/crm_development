from pydantic import BaseModel, EmailStr


class CustomerBase(BaseModel):
    name : str
    phone : str
    email : EmailStr
    website : str | None = None
    address : str


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name : str | None = None
    phone : str | None = None
    email : str | None = None
    website : str | None = None
    address : str | None = None