from crud.models import UsersDAO
from core.auth.security import verify_password

async def authenticate_user(email: str, password: str):
    email = email.strip().lower()
    user = await UsersDAO.find_one_or_none(email=email)
    print(user)

    if not user:
        return None
    
    if not verify_password(password,user.hashed_password):
        return None
    
    return user