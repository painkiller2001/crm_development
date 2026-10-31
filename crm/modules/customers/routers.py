from fastapi import APIRouter


router = APIRouter(prefix='/customers')


@router.post('')
async def create_customer():
    ...


@router.get('')
async def get_customers():
    ...


@router.get('')
async def get_customer():
    ...


@router.put('')
async def update_customer():
    ...


@router.delete('')
async def delete_customer():
    ...
