from fastapi import FastAPI
from app.api.endpoints.user import router as user_router
from app.api.endpoints.dish import router as dish_router


def include_routes(app: FastAPI):
    app.include_router(user_router)
    app.include_router(dish_router)

