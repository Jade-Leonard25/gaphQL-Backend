from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
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

class DBChat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class DBContent(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chats.id"))
    content = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

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


class ContentBase(BaseModel):
    content: dict


class ContentCreate(ContentBase):
    pass


class Content(ContentBase):
    id: int
    chat_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ChatBase(BaseModel):
    pass


class ChatCreate(ChatBase):
    pass


class Chat(ChatBase):
    id: int
    created_at: datetime
    contents: list[Content] = []

    model_config = ConfigDict(from_attributes=True)