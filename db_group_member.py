from sqlalchemy.orm.session import Session
from db.models import Message, Group, GroupMember
import schemas.DbUser


def add_member_to_group(db: Session, group_id: int, user_id: int, is_admin: bool = True):
    db_group = db.query(Group).filter(Group.id == group_id).first()
    
    if db_group:
        # Check if the user is already a member
        existing_member = db.query(GroupMember).filter(GroupMember.group_id == group_id, GroupMember.user_id == user_id).first()
        if existing_member:
            return {"msg": "User already a member of this group"}
        
        db_member = GroupMember(group_id=group_id, user_id=user_id, is_admin=is_admin)
        db.add(db_member)
        db.commit()
        db.refresh(db_member)
        return db_member
    return {"msg": "Group not found"}
