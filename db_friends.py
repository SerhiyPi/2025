from db.db_user import DbUser
from db.hashing import Hash
from fastapi import HTTPException
from sqlalchemy.exc import IdentifierError
from starlette import status
from sqlalchemy.orm import Session
from routers.schemas import Friend_Request
from db.database import get_db
from db.models import DbFriendship


# To send a friend request

def send_request(db: Session, request: Friend_Request):
   user = db.query(DbUser).filter(DbUser.id == request.user_id).first()
if not DbUser:
     raise ValueError(f"User with id {request.user_id} not found")
     
new_friend = db.query(DbUser).filter(DbUser.id == request.new_friend_id).first()

if not new_friend:

        raise ValueError(f"User with id {request.new_friend_id} not found")


friendship = db.query(DbFriendship).filter(DbFriendship.user_id == request.user_id).first()

if not friendship:
    friendship = DbFriendship(user_id=request.user_id, friend_id=request.new_friend_id)
    db.add(friendship)
    db.commit()
    db.refresh(friendship)

else:
    friendship.requests.append(request.new_friend_id)
    db.commit()

    #return {"message": "Friend request sent successfully"}           

    
    
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