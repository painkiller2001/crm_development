from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

from crm.core.database import get_db
from crm.modules.users import crud
from sqlalchemy.future import select
from crm.core.security import verify_password, create_access_token 

from .schema import UserCreate, UserUpdate

from .models import UserModel


router = APIRouter(tags=["Auth"])


@router.post('/login')
async def login(login_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(UserModel).filter(UserModel.email == login_data.username))
    user = result.scalars().first()

    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        access_token = create_access_token(data={"sub": user.email})
        return {"access_token": access_token, "token_type": "bearer"}
