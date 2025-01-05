from configparser import InterpolationMissingOptionError
from turtle import title
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from sqlalchemy import DateTime
from fastapi import Depends, HTTPException
from db.database import engine
from sqlalchemy.orm import Session
from db.models import DbUser



class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  username: str
  email: str
  class Config():
    orm_mode = True

# For PostDisplay

class User(BaseModel):
  username: str
  class Config():
    orm_mode = True

# For PostDisplay

class Comment(BaseModel):
  text: str
  username: str
  timestamp: datetime 
  class Config():
    orm_mode = True

class PostDisplay(BaseModel):
  title: str
  content: str
  timestamp: datetime
  user: User
  comments: List[Comment]
  
  class Config():
    orm_mode = True
    
class PostBase(BaseModel):
  title: str
  content: str
  user_id: int

class UserAuth(BaseModel):
  id: int
  username: str
  email: str

class CommentBase(BaseModel):
  text: str
  username: str
  post_id: int

# For Groups

class GroupBase(BaseModel):
    name: str
    description : str
    admin_id : int
 
class GroupResponse(BaseModel):
        id: int
        admin: UserDisplay
        is_admin: bool
 
        class Config:
            from_attributes = True
  
class MessageBase(BaseModel):
    content: str
 
class MessageCreate(BaseModel):
    content: str
    group_id: int
    sender_id: int
    receiver_id: int
 
class MessageResponse(BaseModel):
    id: int
    timestamp: Optional[datetime] = datetime.now()
 
    class Config:
        from_attributes = True  

class Friend_Request(BaseModel):
    user_id: int
    new_friend_id: int

