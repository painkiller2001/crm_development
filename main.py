from fastapi import FastAPI
from crm.modules.users.routers import router as users_router

app = FastAPI(title="CRM System")

app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "CRM API работает!"}