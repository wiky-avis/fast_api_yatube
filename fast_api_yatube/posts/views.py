from typing import List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from . import models, schemas

api = NinjaAPI()


@api.get('/group', response=List[schemas.Group])
def get_group(request):
    return models.Group.objects.all()


@api.get('/post', response=List[schemas.Post])
def get_posts(request):
    return models.Post.objects.all()


@api.get('/post/{post_pk}', response=schemas.Post)
def get_post(request, post_pk: int):
    return get_object_or_404(models.Post, id=post_pk)


@api.post('/comment')
def create_comment(request, comment: schemas.Comment):
    return models.Comment.objects.create(**comment.dict())
