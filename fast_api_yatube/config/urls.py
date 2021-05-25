from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from auth.views import api_auth
from posts.views import posts

api = NinjaAPI()

api.add_router('/', posts)
api.add_router('auth/', api_auth)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls),
]
