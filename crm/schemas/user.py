from pydantic import BaseModel


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    role: str
    department: str