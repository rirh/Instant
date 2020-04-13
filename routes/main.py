
from django.http import HttpResponse
import json


def get_ip(request):
    # result = {
    #     "": "hello world"
    # }
    return HttpResponse('ping')
