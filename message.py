from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import models
from db.database import get_db
from db.models import GroupMember, Group, DbUser
from routers.schemas import MessageResponse, MessageCreate
from routers import group_member, post, comment, message, group, group_member

router = APIRouter( 
    prefix='/message',
    tags=['message']
)



@router.post("/messages/", response_model=MessageResponse)
def send_message(message: MessageCreate, db: Session = Depends(get_db)):
    return db_message.create_message(db=db, message=message)