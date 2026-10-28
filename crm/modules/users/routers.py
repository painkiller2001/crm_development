from fastapi import APIRouter, Depends


router = APIRouter()


@router.post('/users/create')
async def create_user():
    ...


@router.get('/users/')
async def get_users():
    ...


@router.get('/users/{id}')
async def get_user(id: int):
    ...


@router.put('/users/update/{id}')
async def update_user(id: int):
    ...


@router.post('/users/delete/{id}')
async def delete_user(id: int):
    ...
