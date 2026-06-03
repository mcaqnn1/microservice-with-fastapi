from fastapi import APIRouter,Response,HTTPException,status,Depends
from core.auth.security import create_access_token
from schemas.users import UserLogin
from core.auth.authentication import authenticate_user
from api.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["AUTH-LOGIN"]
)

@router.post("/login/")
async def login_user(response:Response,user_data:UserLogin):
    user = await authenticate_user(user_data.email,user_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User does not exist!",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    access_token = create_access_token({"sub":str(user.id)})
    response.set_cookie(
        "access_token",
        access_token,
        httponly=True
    )
    return {
        "message":"Successful!"
    }

@router.get("/")
async def get_me(current_user=Depends(get_current_user)):
    return current_user

@router.post("/signout")
async def sign_out(response:Response):
    await response.delete_cookie("access_token")