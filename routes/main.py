
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
import rest.Base
import json


def time(request):
    timer = rest.Base.Timer()
    serializer = rest.Base.TimerSerializer(timer)
    json = JSONRenderer().render(serializer.data)
    return HttpResponse(json)


def add_list(request):
    return


def delete_list(request):
    return


def update_list(request):
    pass


def query_list(request):
    return
