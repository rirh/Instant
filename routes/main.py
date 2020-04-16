
from django.http import HttpResponse
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.renderers import JSONRenderer
import rest.Base
import json


@api_view(['get'])
def time(request):
    return HttpResponse(rest.Base.time)


@api_view(['post'])
def add_list(request):
    print(request.data)
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")


@api_view(['delete'])
def delete_list(request):
    print(request.data)
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")


@api_view(['put'])
def update_list(request):
    print(request.data)
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")


@api_view(['get'])
def query_list(request):
    print(request.data)
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")
