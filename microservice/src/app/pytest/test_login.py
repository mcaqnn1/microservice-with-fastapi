import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(app=app, base_url="https://test") as ac:

        response = await ac.post("/login/", json = {
            "email":"test@gmail.com",
            "hashed_password":"test"
        })
        
    assert response.status_code==200
    assert response.json() == {"message":"Successful!"}