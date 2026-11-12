from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    first_name: str
    last_name: str
    role: str
    department: str
    email : EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    role: str | None = None
    department: str | None = None
    email : EmailStr | None = None
    password: str | None = None