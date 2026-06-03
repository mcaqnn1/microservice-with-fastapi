from core.db.config import Base
from sqlalchemy import Column,String,Integer,Boolean
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    full_name = Column(String,nullable=False,index=True)
    email = Column(String,nullable=False,unique=True,index=True)
    hashed_password = Column(String,nullable=False)
    is_activate = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    items = relationship("Items",back_populates="owner", lazy="selectin")