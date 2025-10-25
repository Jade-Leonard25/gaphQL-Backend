from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from schema import schema
from typing import List

router = APIRouter(
    prefix="/chats",
    tags=["chats"],
)

@router.post("/", response_model=schema.Chat)
def create_chat(db: Session = Depends(get_db)):
    new_chat = schema.DBChat()
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat

@router.get("/", response_model=List[schema.Chat])
def get_all_chats(db: Session = Depends(get_db)):
    return db.query(schema.DBChat).all()

@router.get("/{chat_id}", response_model=schema.Chat)
def get_chat(chat_id: int, db: Session = Depends(get_db)):
    chat = db.query(schema.DBChat).filter(schema.DBChat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat

@router.post("/{chat_id}/contents/", response_model=schema.Content)
def create_content_for_chat(
    chat_id: int, content: schema.ContentCreate, db: Session = Depends(get_db)
):
    chat = db.query(schema.DBChat).filter(schema.DBChat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    new_content = schema.DBContent(**content.model_dump(), chat_id=chat_id)
    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    return new_content
