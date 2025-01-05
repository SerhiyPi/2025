from sqlalchemy.orm.session import Session
from db.models import  Message, Group, GroupMember
from routers import schemas


def create_group(db: Session, group: schemas.GroupBase):
    db_group = Group(
        name=group.name,
        description=group.description,
        admin_id=group.admin_id
    )
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

