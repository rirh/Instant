from django.urls import path

from . import views
from app.app import find_app, post_app

urlpatterns = [
    path(r'list/', find_app),
    path(r'post_list/', post_app),
]
