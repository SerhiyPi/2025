from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import db_friends 
from db.database import get_db
from db.models import DbUser
from routers.schemas import Friend_Request


router = APIRouter(
    prefix="/friends",
    tags=["friends"]
)

@router.get('/{id}')
def get_friends(id: int, db: Session = Depends(get_db)):
    return db_friends.get_friends(id, db)


@router.put("/{id}/send")
def send_friend_request(id: int, request: Friend_Request, db: Session = Depends(get_db)):
    return db_friends.send_request(db=db, request=request)


#@router.put("/{id}/aprove")
#def approve_friend_request(id: int, request: Friend_Request, db: Session = Depends(get_db)):
   # return db_user.approve_request(db=db, request=request, id=id)

@router.put("/friends/{id}/approve")
def approve_request(id: int, request: Friend_Request, db: Session = Depends(get_db)):
    return db_friends.approve_request(db=db, request=request, id=id)

@router.put("/{id}/deny")
def dreny_friend_request(id: int, request: Friend_Request, db: Session = Depends(get_db)):
    return db_friends.deny_request(db=db, request=request, id=id)