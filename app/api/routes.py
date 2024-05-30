from fastapi import FastAPI
from app.api.endpoints.user import router as user_router


def include_routes(app: FastAPI):
    app.include_router(user_router)
