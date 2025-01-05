from argparse import _get_action_name
from mailbox import Message
from tokenize import group
from fastapi import FastAPI
from db import models
from db.database import engine
from routers import group_member, user,post,comment,message,group,group_member ,friends
from Auth import authentication

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentication.router)
app.include_router(comment.router)
app.include_router(group_member.router)
app.include_router(group.router)
app.include_router(message.router)
app.include_router(friends.router)

 
users = {}
groups = {}

@app.get('/')
def root():
    return "Hello World!"

models.Base.metadata.create_all(engine)