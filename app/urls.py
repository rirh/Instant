from django.urls import path

from . import views
from app.app import drug_connect, find_app, post_app, query_app, update_app, get_all_ticker, get_specific_ticker, get_kline, get_depth, get_asset_valuation, get_account_info, get_position_swap,get_instruments
from app.app import *
from app.views import add_list, delete_list, update_list, query_list

urlpatterns = [
    path(r'list/', find_app),
    path(r'post_list/', post_app),
    path(r'query_list/', query_app),
    path(r'add_list/', add_list),
    path(r'delete_list/', delete_list),
    path(r'update_list/', update_app),
    path(r'get_all_ticker/', get_all_ticker),
    path(r'get_specific_ticker/', get_specific_ticker),
    path(r'get_kline/', get_kline),
    path(r'get_depth/', get_depth),
    path(r'get_asset_valuation/', get_asset_valuation),
    path(r'get_account_info/', get_account_info),
    path(r'get_position_swap/', get_position_swap),
    path(r'get_instruments/', get_instruments),
    path(r'get_order_list/', get_order_list),
    path(r'get_rate/', get_rate),



    # path(r'query_list/', query_list),
    path(r'<int:question_id>/vote/', query_list),
    path(r'drug_connect/', drug_connect),
]
