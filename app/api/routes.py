from fastapi import FastAPI
from app.api.endpoints.user import router as user_router
from app.api.endpoints.dish import router as dish_router
from app.api.endpoints.drink import router as drink_router


def include_routes(app: FastAPI):
    app.include_router(user_router)
    app.include_router(dish_router)
    app.include_router(drink_router)
