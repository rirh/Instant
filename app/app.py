from django.http import HttpResponse,JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes
import json
from app.models import Crypto


@api_view(['get'])
def find_app(request):
    result = Crypto.objects.filter(name="小花")

    return HttpResponse(123)


@api_view(['post'])
def post_app(request):
    print(request.data)
    name = request.data.get('name')
    age = request.data.get('age')
    sex = request.data.get('sex')
    r1 = Crypto(name=name, age=age, sex=sex)
    r1.save()
    # result = Crypto.objects.get(name='小花')
    # print(result)
    return HttpResponse('')


@api_view(['post'])
def query_app(request):
    print(request.data)
    name = request.data.get('name')
    result = (Crypto.objects.filter(name=name))
    print(type(result))
   
    return HttpResponse(list(result))
