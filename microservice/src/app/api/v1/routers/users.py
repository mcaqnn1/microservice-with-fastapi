from fastapi import APIRouter,HTTPException,status
from crud.models import UsersDAO
from fastapi_cache.decorator import cache
from schemas.users import UserUpdate
from core.auth.security import get_password_hash
import asyncio

router = APIRouter(
    prefix="/auth",
    tags=["AUTH-USERS"]
)

@router.get("/users/")
async def get_all_users():
    users = await UsersDAO.find_all()
    return users

@router.get("/{id}/")
@cache(expire=30)
async def get_by_id(user_id:int):
    await asyncio.sleep(3)
    user_by_id = await UsersDAO.find_by_id(user_id)
    if not user_by_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not by ID!"
        )
    return user_by_id

@router.put("/update/{id}/")
async def update_data(id: int,user_data:UserUpdate):
    existing_user = await UsersDAO.find_one_or_none(id=id)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found!"
        )
    password_hashh = get_password_hash(user_data.password)
    await UsersDAO.update(
        id=id,
        email=user_data.email,
        hashed_password=password_hashh
    )
    return {
        "message":"Successful!"
    }

@router.delete("/delete/{id}/")
async def delete_user(id: int):
    user = await UsersDAO.find_one_or_none(id=id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    await UsersDAO.delete(id=id)
    return {
        "message":"Successful!"
    }