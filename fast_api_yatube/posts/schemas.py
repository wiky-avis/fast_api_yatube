from datetime import datetime

from django.contrib.auth import get_user_model
from ninja import Schema

User = get_user_model()


class UserN(Schema):
    id: int
    username: str


class Group(Schema):
    id: int
    title: str


class Post(Schema):
    id: int
    text: str
    pub_date: datetime
    author: UserN
    image: str
    group: Group


class CreateComment(Schema):
    author_id: int = None
    post_id: int = None
    text: str
    created: datetime


class Comment(CreateComment):
    id: int
