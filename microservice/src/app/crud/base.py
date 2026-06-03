from core.db.config import AsyncSessionLocal
from sqlalchemy import select,insert,update,delete

class BaseService:
    model = None

    @classmethod
    async def find_all(cls):
        async with AsyncSessionLocal() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
    
    @classmethod
    async def find_by_id(cls,id:int):
        async with AsyncSessionLocal() as session:
            query = select(cls.model).filter_by(id=id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
    @classmethod
    async def find_one_or_none(cls, **filter):
        async with AsyncSessionLocal() as session:
            query = select(cls.model).filter_by(**filter)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add(cls, **data):
        async with AsyncSessionLocal() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls,id:int,**data):
        async with AsyncSessionLocal() as session:
            query = update(cls.model).where(cls.model.id == id).values(**data)
            await session.execute(query)
            await session.commit()
    
    @classmethod
    async def delete(cls, **data):
        async with AsyncSessionLocal() as session:
            query = delete(cls.model).filter_by(**data)
            await session.execute(query)
            await session.commit()

        

    



    