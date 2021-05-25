from datetime import datetime

from django.contrib.auth import get_user_model
from ninja import Schema

User = get_user_model()


class UserN(Schema):
    id: int
    username: str


class CreateGroup(Schema):
    title: str


class Group(CreateGroup):
    id: int


class Post(Schema):
    id: int
    text: str
    pub_date: datetime
    author: UserN
    image: str
    group: Group


class CreateComment(Schema):
    text: str


class Comment(CreateComment):
    id: int
    post_id: int = None
    author_id: int = None
    created: datetime
