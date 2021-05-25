from django.contrib import admin
from django.urls import path
from posts.views import posts
from auth.views import api_auth
from ninja import NinjaAPI

api = NinjaAPI()

api.add_router('/', posts)
api.add_router('auth/', api_auth)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls),
]
