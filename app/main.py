from fastapi import FastAPI
from app.core.config import DATABASE_URL
from app.db.session import Base, engine

print(DATABASE_URL)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ecommerce API")

@app.get("/")
def root():
    return {"message": "Ecommercr API is running"}



