from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import models
from db.database import get_db
from db.models import GroupMember, Group, DbUser
from routers.schemas import GroupResponse, GroupBase
from routers import group_member, post, comment, message, group

router = APIRouter( 
    prefix='/group_member',
    tags=['group_member']
)

@router.post("/groups/{group_id}/members/{user_id}")
def add_member(group_id: int, user_id: int, db: Session = Depends(get_db)):
    if not group_id or not user_id:
        return {"msg": "Group ID and User ID are required"}
    
    member = db_group_member.add_member_to_group(db, group_id, user_id)
    if member:
        return {"msg": "Member added successfully"}
    
    raise HTTPException(status_code=404, detail="Group or User not found")
 
@router.get("/groups/{group_id}/members/")
def list_members(group_id: int, db: Session = Depends(get_db)):
    db_group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if not db_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
 
    members = db.query(models.GroupMember).filter(models.GroupMember.group_id == group_id).all()
 
    members_details = []
    for member in members:
        user = db.query(models.User).filter(models.User.id == member.user_id).first()
        if user:
            members_details.append({
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "is_admin": member.is_admin
            })
 
    return {"group_id": group_id, "members": members_details}