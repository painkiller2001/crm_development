from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str
    role: str
    department: str
    email : EmailStr


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    pass


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    role: str | None = None
    department: str | None = None
    email : EmailStr | None = None