from urllib import request
from db.models import DbUser
from routers.schemas import UserBase
from sqlalchemy.orm import Session
from db.hashing import Hash
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from starlette import status
from routers.schemas import Friend_Request


def create_user(request: UserBase, db: Session):
    new_user = DbUser(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db: Session, username: str):
  user = db.query(DbUser).filter(DbUser.id == id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f'User with username {username} not found')
  return user
def send_request(id: int, request: DbUser, db: Session):
    user = db.query(DbUser).filter(DbUser.id == request.id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {request.id} not found"
        )
    









def send_request(db: Session, request: Friend_Request):
    # Validate the user_id
    user = db.query(DbUser).filter(DbUser.id == request.user_id).first()
    if not user:
        raise ValueError(f"User with id {request.user_id} not found")

    # Validate the new_friend_id
    new_friend = db.query(DbUser).filter(DbUser.id == request.new_friend_id).first()
    if not new_friend:
        raise ValueError(f"User with id {request.new_friend_id} not found")

    # Process the friend request
    # Add logic to handle friend request creation, e.g., saving to the database
    return {"message": "Friend request sent successfully"}

    # To approve a friend request

    
def approve_request(id: int, request: Friend_Request, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    
    if request.new_friend_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Friend request not found"
        )