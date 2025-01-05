from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from db.models import DbUser
from routers.schemas import UserDisplay
from db import db_user
from routers.schemas import UserBase
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from routers.schemas import Friend_Request
from db.database import get_db


router = APIRouter(
    prefix='/user',
    tags=['user']
)
@router.post('',response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(request, db)



@router.post("/friend-request/")
def create_friend_request(request: Friend_Request, db: Session = Depends(get_db)):
    return db_user.send_request(db=db, request=request)





    
        
