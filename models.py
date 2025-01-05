import datetime
from turtle import title
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, Integer, String, DateTime,Boolean, table
from sqlalchemy.orm import relationship
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
import datetime
from turtle import title
from datetime import datetime
from pydantic import BaseModel
from db.database import Base

Base = declarative_base()

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('DbPost', back_populates='user')
    group_members = relationship('GroupMember', back_populates='user')
    groups = relationship('Group', secondary='group_members', back_populates='members')



class DbPost(Base):
  __tablename__ = 'post'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  content = Column(String)
  timestamp = Column(DateTime)
  user_id = Column(Integer, ForeignKey('user.id'))
  user = relationship('DbUser', back_populates='items')
  comments = relationship('DbComment', back_populates='post')

class DbComment(Base):
  __tablename__ = 'comment'
  id = Column(Integer, primary_key=True, index=True)
  text = Column(String)
  username = Column(String)
  timestamp = Column(DateTime)
  post_id = Column(Integer, ForeignKey('post.id'))
  post = relationship('DbPost', back_populates='comments')

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    admin_id = Column(Integer, ForeignKey('user.id'))
    admin = relationship('DbUser', backref='admin_groups')
    group_members = relationship('GroupMember', back_populates='group')
    members = relationship('DbUser', secondary='group_members', back_populates='groups')

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    sender_id = Column(Integer, ForeignKey('user.id'))
    receiver_id = Column(Integer, ForeignKey("user.id"))
    
 
class GroupMember(Base):
    __tablename__ = "group_members"
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    is_admin = Column(Boolean, default=False)
    user = relationship('DbUser', back_populates='group_members')  # Ensure the name matches in DbUser
    group = relationship('Group', back_populates='group_members')  # Ensure the name matches in Group


class DbFriendship(Base):
    __tablename__ = 'friendship'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    friend_id = Column(Integer, ForeignKey('user.id'), nullable=False)

#class DbFriendships(Base):
    ##__tablename__ = 'friendships'
    #id = Column(Integer, primary_key=True, index=True)
    #user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    #friend_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    #friend_request = Column(Integer, nullable=True)

class FriendRequest(Base):
    __tablename__ = "friend_requests"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    new_friend_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("DbUser", foreign_keys=[user_id])
    new_friend = relationship("DbUser", foreign_keys=[new_friend_id])