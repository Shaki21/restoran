import uvicorn
from fastapi import FastAPI
from api.routes import include_routes
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from core.database import Base, engine


app = FastAPI()

# Ukljuci sve rute
include_routes(app)

Base.metadata.create_all(bind=engine)

origins = {
    "http://localhost"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return RedirectResponse(url="/docs")
