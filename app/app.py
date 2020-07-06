from app.ak import api_key, secret_key, passphrase
from django.core.serializers import serialize
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes
import json
from app.models import Crypto
import exchange.okex.spot_api as spot
import exchange.okex.account_api as account
import exchange.okex.futures_api as future
import exchange.okex.lever_api as lever
import exchange.okex.swap_api as swap
import exchange.okex.index_api as index
import exchange.okex.option_api as option
import exchange.okex.system_api as system
import time
from urllib import parse
# api_key = "105efe25-6f5e-4335-83c6-a11409af7a6b"
# secret_key = "A877DAEA07C3C023C08789EE45B2C454"
# passphrase = "0x0001"
from dwebsocket.decorators import accept_websocket
@accept_websocket
def crypto_connect(request):
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

    # result = swapAPI.take_order('EOS-USDT-SWAP', '1', '0.1', '1', order_type='0', client_oid='tigerzh', match_price='0')
@api_view(['get'])
def revoke_order(request):
    client_oid = request.GET.get('client_oid')
    print(client_oid)
    swapAPI = swap.SwapAPI(api_key, secret_key, passphrase, False)
    result = swapAPI.revoke_order('', client_oid)
    return HttpResponse(json.dumps(result), content_type="application/json")

@api_view(['get'])
def take_order(request):
    instrument_id = request.GET.get('instrument_id')
    order_type = request.GET.get('order_type')
    type = request.GET.get('type')
    size = request.GET.get('size')
    match_price = request.GET.get('match_price')
    price = request.GET.get('price')
    client_oid = 'crypto'+str(int(time.time()))
    print(client_oid)
    swapAPI = swap.SwapAPI(api_key, secret_key, passphrase, False)
    result = swapAPI.take_order(
        instrument_id, type, price, size, client_oid, order_type, match_price)
    return HttpResponse(json.dumps(result), content_type="application/json")


@api_view(['get'])
def get_rate(request):
    swapAPI = swap.SwapAPI(api_key, secret_key, passphrase, False)
    result = swapAPI.get_rate()
    return HttpResponse(json.dumps(result), content_type="application/json")


@api_view(['get'])
def get_order_list(request):
    swapAPI = swap.SwapAPI(api_key, secret_key, passphrase, False)
    instrument_id = request.GET.get('instrument_id')
    state = request.GET.get('state')
    result = swapAPI.get_order_list(instrument_id, state)
    return HttpResponse(json.dumps(result), content_type="application/json")


@api_view(['get'])
def get_instruments(request):
    swapAPI = swap.SwapAPI(api_key, secret_key, passphrase, False)
    result = swapAPI.get_instruments()
    return HttpResponse(json.dumps(result), content_type="application/json")


@api_view(['get'])
def get_position_swap(request):
    swapAPI = swap.SwapAPI(api_key, secret_key, passphrase, False)
    result = swapAPI.get_position()
    return HttpResponse(json.dumps(result), content_type="application/json")


@api_view(['get'])
def get_account_info(request):
    account_type = request.GET.get('account_type')
    if account_type == '1':
        spotAPI = spot.SpotAPI(api_key, secret_key, passphrase, False)
    # 币币账户信息 （20次/2s）
        result = spotAPI.get_account_info()
    elif account_type == '3':
        futureAPI = future.FutureAPI(api_key, secret_key, passphrase, False)
        result = futureAPI.get_accounts()
    elif account_type == '6':
        accountAPI = account.AccountAPI(api_key, secret_key, passphrase, False)
        result = accountAPI.get_wallet()
    elif account_type == '8':
        accountAPI = account.AccountAPI(api_key, secret_key, passphrase, False)
        result = accountAPI.get_wallet()
    elif account_type == '9':
        swapAPI = swap.SwapAPI(api_key, secret_key, passphrase, False)
        result = swapAPI.get_accounts()
    elif account_type == '16':
        swapAPI = swap.SwapAPI(api_key, secret_key, passphrase, False)
        result = swapAPI.get_accounts()
    else:
        request = ({})
    return HttpResponse(json.dumps(result), content_type="application/json")


@api_view(['get'])
def get_asset_valuation(request):
    accountAPI = account.AccountAPI(api_key, secret_key, passphrase, False)
    result = accountAPI.get_asset_valuation(0, 'USD')
    return HttpResponse(json.dumps(result), content_type="application/json")


@api_view(['get'])
def get_depth(request):
    instrument_id = request.GET.get('instrument_id')
    size = request.GET.get('size')
    spotAPI = spot.SpotAPI(api_key, secret_key, passphrase, False)
    result = spotAPI.get_depth(instrument_id, size)
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
