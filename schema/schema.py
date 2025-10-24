from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from db.db import Base
from typing import Optional

# SQLAlchemy Model
class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    address = Column(String)
    city = Column(String)
    hashed_password = Column(String)
    createdat = Column(DateTime, default=datetime.utcnow)
    updatedat = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    contact_number = Column(String)

# Pydantic Schemas
class UserBase(BaseModel):
    email: str
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    contact_number: Optional[str] = None

class UserCreate(UserBase):
    password: str
    confirm_password: str

class UserUpdate(BaseModel):
    password: Optional[str] = None
    confirm_password: Optional[str] = None

class UserLogin(BaseModel):
    email: str
    password: str

class User(UserBase):
    id: int
    createdat: datetime
    updatedat: datetime

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None