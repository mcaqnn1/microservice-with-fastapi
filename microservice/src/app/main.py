from fastapi import FastAPI
from app.api.v1.routers.register import router as register_router
from api.v1.routers.users import router as users_router
from api.v1.routers.login import router as login_user
from worker import lifespan
import uvicorn

app = FastAPI(
    title="Microservice with FastAPI",
    lifespan=lifespan
)

app.include_router(register_router)
app.include_router(login_user)
app.include_router(users_router)

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)