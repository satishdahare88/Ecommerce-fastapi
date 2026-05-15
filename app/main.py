from fastapi import FastAPI
from app.core.config import DATABASE_URL
from app.db.session import Base, engine
from app.models.user import User
from app.api.routes.auth import router as auth_router 

app = FastAPI(title="Ecommerce API")
app.include_router(auth_router)

print(DATABASE_URL)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Ecommercr API is running"}
