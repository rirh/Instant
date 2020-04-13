
from django.http import HttpResponse
from exchange.okex import account
import json
import logging
import datetime

def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"


time = get_timestamp()
if __name__ == '__main__':

    api_key = "105efe25-6f5e-4335-83c6-a11409af7a6b"
    secret_key = "A877DAEA07C3C023C08789EE45B2C454"
    passphrase = "0x0001"


# Create your views here.
def index(request):
    accountAPI = account.AccountAPI(api_key, secret_key, passphrase, False)
    result = accountAPI.get_wallet()
    return HttpResponse(json.dumps(result))
