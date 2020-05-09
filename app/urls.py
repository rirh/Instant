from django.urls import path

from . import views
from app.app import find_app, post_app, query_app, update_app, get_coin_info
from app.views import add_list, delete_list, update_list, query_list

urlpatterns = [
    path(r'list/', find_app),
    path(r'post_list/', post_app),
    path(r'query_list/', query_app),
    path(r'add_list/', add_list),
    path(r'delete_list/', delete_list),
    path(r'update_list/', update_app),
    path(r'get_coin_info/', get_coin_info),
    # path(r'query_list/', query_list),
    path(r'<int:question_id>/vote/', query_list),
]
