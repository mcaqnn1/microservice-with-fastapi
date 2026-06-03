from fastapi import APIRouter,HTTPException,status
from schemas.users import UserCreate
from crud.models import UsersDAO
from core.auth.security import get_password_hash

router = APIRouter(
    prefix="/auth",
    tags=["AUTH-REGISTRATION"]
)

@router.post("/register/")
async def register_user(user_data:UserCreate):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists!"
        )
    
    password_hash = get_password_hash(user_data.password)

    await UsersDAO.add(
        full_name=user_data.full_name,
        email=user_data.email,
        hashed_password=password_hash
    )

    return {
        "message":"Registration successful!"
    }