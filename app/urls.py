from django.urls import path

from . import views
from app.app import find_app, post_app
from app.views import add_list, delete_list, update_list, query_list

urlpatterns = [
    path(r'list/', find_app),
    path(r'post_list/', post_app),
    path(r'add_list/', add_list),
    path(r'delete_list/', delete_list),
    path(r'update_list/', update_list),
    path(r'query_list/', query_list),
    path(r'<int:question_id>/vote/', query_list),
]
