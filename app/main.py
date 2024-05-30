import uvicorn
from fastapi import FastAPI
from app.api.routes import user_router
from app.core.database import engine, Base
from fastapi.responses import RedirectResponse

app = FastAPI()

# Kreiraj sve tablice u bazi
Base.metadata.create_all(bind=engine)

# Ukljuci rutu za korisnike
app.include_router(user_router, prefix="/users", tags=["users"])


@app.get("/")
async def home():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
