from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"


class Department(str, Enum):
    SALES = "sales"
    SUPPORT = "support"
    DEV = "dev"