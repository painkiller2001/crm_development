from fastapi import FastAPI

from crm.modules.customers.routers import router as customers_router
from crm.modules.users.routers import router as users_router

app = FastAPI(title="CRM System")

app.include_router(users_router)
app.include_router(customers_router)


@app.get("/")
async def root():
    return {"message": "CRM API работает!"}