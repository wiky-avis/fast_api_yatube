from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from auth.jwt import AuthBearer

from . import models, schemas

posts = Router()


@posts.get('/group', response=List[schemas.Group])
def get_groups(request):
    return models.Group.objects.all()


@posts.get('/group/{group_id}/posts', response=List[schemas.Post])
def get_group_posts(request, group_id: int):
    return models.Post.objects.filter(group__id=group_id)


@posts.post('/group', response=schemas.Group, auth=AuthBearer())
def create_group(request, group: schemas.CreateGroup):
    return models.Group.objects.create(**group.dict())


@posts.put('/group/{group_id}', response=schemas.Group, auth=AuthBearer())
def update_group(request, group_id: int, group: schemas.CreateGroup):
    _group = get_object_or_404(
        models.Group, id=group_id)
    _group.title = group.title
    _group.save()
    return _group


@posts.delete('/group/{group_id}', auth=AuthBearer())
def delete_comment(request, group_id: int):
    _group = get_object_or_404(
        models.Group, id=group_id)
    _group.delete()
    return {'success': 204}


@posts.get('/post', response=List[schemas.Post])
def get_posts(request):
    return models.Post.objects.all()


@posts.get('/post/{post_pk}', response=schemas.Post)
def get_post(request, post_pk: int):
    return get_object_or_404(models.Post, id=post_pk)


@posts.get('/{post_id}/comment', response=List[schemas.Comment])
def get_comments(request, post_id: int):
    return models.Comment.objects.filter(post__id=post_id)


@posts.post('/{post_id}/comment', response=schemas.Comment, auth=AuthBearer())
def create_comment(request, post_id: int, comment: schemas.CreateComment):
    return models.Comment.objects.create(
        author=request.auth, post_id=post_id, **comment.dict())


@posts.put(
    '/{post_id}/comment/{comment_id}',
    response=schemas.Comment,
    auth=AuthBearer())
def update_comment(request, comment_id: int, comment: schemas.CreateComment):
    _comment = get_object_or_404(
        models.Comment, id=comment_id, author=request.auth)
    _comment.text = comment.text
    _comment.save()
    return _comment


@posts.delete(
    '/{post_id}/comment/{comment_id}', auth=AuthBearer())
def delete_comment(request, comment_id: int):
    _comment = get_object_or_404(
        models.Comment, id=comment_id, author=request.auth)
    _comment.delete()
    return {'success': 204}
