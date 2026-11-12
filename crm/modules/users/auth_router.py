from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

from crm.core.database import get_db
from crm.modules.users import crud
from sqlalchemy.future import select
from crm.core.security import verify_password, create_access_token 

from .schema import UserCreate, UserUpdate

from .models import UserModel


router = APIRouter(prefix='/users', tags=["Auth"])


@router.post('/login')
async def login():
    ...