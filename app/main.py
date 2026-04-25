from fastapi import FastAPI

app = FastAPI(title="Ecommerce API")

@app.get("/")
def root():
    return {"message": "Ecommercr API is running"}

