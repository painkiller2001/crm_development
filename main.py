from fastapi import FastAPI

from crm.modules.users.routers import router as users_router
from crm.modules.customers.routers import router as customers_router
from crm.modules.deals.routers import router as deals_router

app = FastAPI(title="CRM System")

app.include_router(users_router)
app.include_router(customers_router)
app.include_router(deals_router)


@app.get("/")
async def root():
    return {"message": "CRM API работает!"}