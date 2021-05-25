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


class CreatePost(Schema):
    text: str
    image: str = None
    group_id: int = None


class Post(CreatePost):
    id: int
    pub_date: datetime
    author: UserN


class CreateComment(Schema):
    text: str


class Comment(CreateComment):
    id: int
    post_id: int = None
    author_id: int = None
    created: datetime
