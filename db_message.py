from sqlalchemy.orm.session import Session
from db.models import User, Message, Group, GroupMember
import schemas.user


def create_message(db: Session, message: schemas.user.MessageCreate):
    db_message = Message(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message