from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 

from app.db.dependencies import get_db 
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password, create_acces_token


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):

    existing_user  = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = hash_password(user.password)
    new_user = User(
        email = user.email,
        password = hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if not existing_user:
        raise HTTPException(status_code=401, detail = "Invalid credencials")
    
    if not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=401, detail = "Invalid credentials")
    
    token = create_acces_token(data={"sub": existing_user.email})

    return {"access_token": token, 
            "token_type": "bearer"}
