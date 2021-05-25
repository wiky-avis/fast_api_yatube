from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from . import models, schemas
from auth.jwt import AuthBearer

posts = Router()


@posts.get('/group', response=List[schemas.Group])
def get_group(request):
    return models.Group.objects.all()


@posts.get('/post', response=List[schemas.Post])
def get_posts(request):
    return models.Post.objects.all()


@posts.get('/post/{post_pk}', response=schemas.Post)
def get_post(request, post_pk: int):
    return get_object_or_404(models.Post, id=post_pk)


@posts.get('/{post_id}/comment', response=List[schemas.Comment])
def get_comments(request, post_id: int):
    return models.Comment.objects.filter(post__id=post_id)


@posts.post('/comment', response=schemas.Comment, auth=AuthBearer)
def create_comment(request, comment: schemas.CreateComment):
    return models.Comment.objects.create(
        author=request.auth, **comment.dict())
