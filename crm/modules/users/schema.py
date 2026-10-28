from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    role: str
    department: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    pass


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    role: str | None = None
    department: str | None = None