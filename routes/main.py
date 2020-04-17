
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.renderers import JSONRenderer
import rest
# import rest.base import Timer
# import rest.base import TimerSerializer
import json


@api_view(['get'])
def time(request):
    return HttpResponse(rest.base.time)


@api_view(['post'])
def add_list(request):
    print(request.data)
    if request.data.get('name') == 'POST':
        resp = {'errorcode': 100, 'detail': 'Get success'}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        return HttpResponse(json.dumps({
            'name': '????? wtf, boy arrt name should be POST ok?'
        }), status=status.HTTP_400_BAD_REQUEST)


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
