from app.ak import api_key, secret_key, passphrase
from django.core.serializers import serialize
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes
import json
from app.models import Crypto
import exchange.okex.spot_api as spot
import time
from urllib import parse
# api_key = "105efe25-6f5e-4335-83c6-a11409af7a6b"
# secret_key = "A877DAEA07C3C023C08789EE45B2C454"
# passphrase = "0x0001"
from dwebsocket.decorators import accept_websocket
@accept_websocket
def drug_connect(request):
    if request.is_websocket():
        try:
            messages = {
                'time': time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())),
                'msg': 'send %d times!' % i,
            }
            msg = json.dumps(messages)
            request.websocket.send(msg)
        except Exception as e:
            try:
                request.websocket.close()
                return
            except:
                return

@api_view(['get'])
def get_depth(request):
    instrument_id = request.GET.get('instrument_id')
    size = request.GET.get('size')
    spotAPI = spot.SpotAPI(api_key, secret_key, passphrase, False)
    result = spotAPI.get_depth(instrument_id,size)
    return HttpResponse(json.dumps(result), content_type="application/json")

@api_view(['get'])
def get_all_ticker(request):
    spotAPI = spot.SpotAPI(api_key, secret_key, passphrase, False)
    result = spotAPI.get_ticker()
    return HttpResponse(json.dumps(result), content_type="application/json")


@api_view(['get'])
def get_specific_ticker(request):
    # instrument_id = request.data.get('instrument_id')
    instrument_id = request.GET.get('instrument_id')
    spotAPI = spot.SpotAPI(api_key, secret_key, passphrase, False)
    result = spotAPI.get_specific_ticker(instrument_id)
    return HttpResponse(json.dumps(result), content_type="application/json")


@api_view(['get'])
def get_kline(request):
    # instrument_id = request.data.get('instrument_id')
    instrument_id = request.GET.get('instrument_id')
    start = request.GET.get('start')
    end = request.GET.get('end')
    granularity = request.GET.get('granularity')
    spotAPI = spot.SpotAPI(api_key, secret_key, passphrase, False)
    result = spotAPI.get_kline(instrument_id, granularity)
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
