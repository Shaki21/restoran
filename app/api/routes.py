from fastapi import FastAPI
from app.api.endpoints.user import router as user_router
from app.api.endpoints.dish import router as dish_router
from app.api.endpoints.drink import router as drink_router
from app.api.endpoints.table import router as table_router
from app.api.endpoints.order import router as order_router
from app.api.endpoints.auth import router as auth_router


def include_routes(app: FastAPI):
    app.include_router(user_router)
    app.include_router(dish_router)
    app.include_router(drink_router)
    app.include_router(table_router)
    app.include_router(order_router)
    app.include_router(auth_router)
