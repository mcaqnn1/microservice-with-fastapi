from core.db.config import Base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship

class Items(Base):
    __tablename__ = "items"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False,index=True)
    description = Column(String,index=True)
    owner_id = Column(Integer,ForeignKey("users.id"))
    owner = relationship("Users",back_populates="items")
