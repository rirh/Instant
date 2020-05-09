from django.core.serializers import serialize
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes
import json
from app.models import Crypto
import exchange.okex.spot_api as spot


api_key = "105efe25-6f5e-4335-83c6-a11409af7a6b"
secret_key = "A877DAEA07C3C023C08789EE45B2C454"
passphrase = "0x0001"


@api_view(['get'])
def get_ticker(request):
    spotAPI = spot.SpotAPI(api_key, secret_key, passphrase, False)
    result = spotAPI.get_ticker()
    return HttpResponse(json.dumps(result), content_type="application/json")



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
    # print(request.data)
    name = request.data.get('name')
    result = Crypto.objects.filter(name=name)
    json_data = serialize('json', result)  # str
    json_data = json.loads(json_data)  # 序列化成json对象
    return HttpResponse(json_data)


@api_view(['post'])
def update_app(request):
    # print(request.data)
    name = request.data.get('name')
    age = request.data.get('age')
    print(type(age))
    result = Crypto.objects.filter(name=name).update(age=age)
    # json_data = serialize('json', result)  # str
    # json_data = json.loads(json_data)  # 序列化成json对象
    return HttpResponse(result)


@api_view(['delete'])
def update_app(request):
    # print(request.data)
    name = request.data.get('name')
    age = request.data.get('age')
    print(type(age))
    result = Crypto.objects.filter(name=name).delete()
    # json_data = serialize('json', result)  # str
    # json_data = json.loads(json_data)  # 序列化成json对象
    return HttpResponse(result)
