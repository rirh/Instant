from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.renderers import JSONRenderer
from rest import base
# import rest.base import Timer
# import rest.base import TimerSerializer
import json
import django.db


# class Person(models.Model):
#     first_name = django.db.models.CharField(max_length=30)
#     last_name = django.db.models.CharField(max_length=30)
#     pass


@api_view(['get'])
def time(request):
    timer = base.Timer()
    serializer = base.TimerSerializer(timer)
    time = JSONRenderer().render(serializer.data)
    return HttpResponse(time)


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
def query_list(request, question_id=0):
    print(request.data, question_id)
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")


# @api_view(['get', 'post', 'put', 'delete', 'patch'])
# def page_not_font(request):
#     resp = {'errorcode': 404, 'detail': 'are you serious???'}
#     return HttpResponse(json.dumps(resp), content_type="application/json")

