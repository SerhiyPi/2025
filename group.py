from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import models
from db.database import get_db
from db.models import GroupMember, Group, DbUser
from routers import schemas
from routers.schemas import  GroupResponse
from routers import group_member, post, comment, message, group, group_member
from db import db_groups

router = APIRouter( 
    prefix='/group',
    tags=['group']
)

@router.post("/groups/", response_model=GroupResponse)
def create_group(group: BaseModel, db: Session = Depends(get_db)):
    return db_groups.create_group(db=db, group=group)








