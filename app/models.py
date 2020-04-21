# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Crypto(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    age = models.IntegerField(default=0)
    sex = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name,\
            self.age,\
            self.sex


class Server_List(models.Model):
    name = models.CharField(max_length=64)
    host = models.CharField(max_length=256, null=True)
    lhost = models.CharField(max_length=32, null=True)
    port = models.CharField(max_length=64, null=True)
    user = models.CharField(max_length=64, null=True)
    pw = models.CharField(max_length=64, null=True)
    db = models.CharField(max_length=64, null=True)
    version = models.CharField(max_length=16, null=True)
    upd = models.CharField(max_length=1, null=True)
    lock_time = models.IntegerField(default=0)
    exchange = models.CharField(max_length=20, null=True)
    symbol = models.CharField(max_length=1024, null=True)

    def __unicode__(self):
        return self.name, \
            self.host, \
            self.lhost, \
            self.port, \
            self.user, \
            self.pw, \
            self.db, \
            self.version, \
            self.upd, \
            self.upd, \
            self.exchange, \
            self.symbol


class Exchange_List(models.Model):
    exchange_type = models.CharField(max_length=1)
    exchange = models.CharField(max_length=64)
    default_brief = models.CharField(max_length=2)
    key1_name = models.CharField(max_length=20, null=True)
    key2_name = models.CharField(max_length=20, null=True)
    key3_name = models.CharField(max_length=20, null=True)
    t_type = models.CharField(max_length=128, null=True)
    get_key_url = models.CharField(max_length=256)
    img_url = models.CharField(max_length=256, null=True)

    def __unicode__(self):
        return self.exchange_type, \
            self.exchange, \
            self.default_brief, \
            self.key1_name, \
            self.key2_name, \
            self.key3_name, \
            self.t_type, \
            self.get_key_url, \
            self.img_url

# class User(models.Model):
#     # 用户表
#     user = models.CharField(primary_key=True, max_length=16)
#     username = models.EmailField(max_length=40, null=True)
#     district = models.CharField(max_length=6, null=True)
#     mobile = models.CharField(max_length=40, null=True)
#     email = models.CharField(max_length=40, null=True)
#     nickname = models.CharField(max_length=16, null=True)
#     type = models.CharField(max_length=10)      # APPLY, NEW, Normal
#     date_s = models.IntegerField(default=0)
#     date_e = models.IntegerField(default=0)
#     i_code = models.CharField(max_length=8)
#     password = models.CharField(max_length=256, null=True)
#     log_user = models.CharField(max_length=16)
#     c_time = models.IntegerField(default=0)
#
#     def __unicode__(self):
#         return self.user, \
#                self.nickname, \
#                self.username, \
#                self.district, \
#                self.mobile, \
#                self.email, \
#                self.type, \
#                self.date_s, \
#                self.date_e, \
#                self.i_code, \
#                self.password, \
#                self.log_user, \
#                self.c_time
#
#     class Meta:
#         ordering = ['c_time']
#         verbose_name = '用户'
#         verbose_name_plural = '用户'


class User2(models.Model):
    # 用户表
    user = models.CharField(max_length=16)
    user_brief = models.CharField(max_length=6)
    username = models.EmailField(max_length=40, null=True)
    district = models.CharField(max_length=6, null=True)
    mobile = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=40, null=True)
    nickname = models.CharField(max_length=16, null=True)
    type = models.CharField(max_length=10)      # APPLY, NEW, Normal
    date_s = models.IntegerField(default=0)
    date_e = models.IntegerField(default=0)
    i_code = models.CharField(max_length=8)
    dealer = models.CharField(max_length=6)
    password = models.CharField(max_length=256, null=True)
    log_user = models.CharField(max_length=16)
    mb = models.CharField(max_length=64, null=True)
    c_time = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user, \
            self.user_brief, \
            self.nickname, \
            self.username, \
            self.district, \
            self.mobile, \
            self.email, \
            self.type, \
            self.date_s, \
            self.date_e, \
            self.i_code, \
            self.password, \
            self.log_user, \
            self.mb, \
            self.c_time

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class User_Code(models.Model):
    # user
    user = models.CharField(
        primary_key=True, max_length=40)    # type TEL, EMAIL
    dev = models.CharField(max_length=6)  # MOBILE, EMAIL
    code = models.CharField(max_length=8)
    c_time = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user, \
            self.dev, \
            self.code, \
            self.c_time


class User_Server(models.Model):
    # 用户服务器对照表
    user = models.CharField(max_length=16)
    s_name = models.CharField(max_length=64)
    s_2nd = models.CharField(max_length=64, unique=True)
    server = models.CharField(max_length=128)
    host = models.CharField(max_length=64)
    valid = models.CharField(max_length=1, null=True)
    date_s = models.IntegerField(default=0)
    date_e = models.IntegerField(default=0)
    log_user = models.CharField(max_length=16, null=True)
    version = models.CharField(max_length=16, null=True)
    c_time = models.IntegerField(default=0)
    token = models.CharField(max_length=64, null=True)

    def __unicode__(self):
        return self.user, \
            self.s_name, \
            self.server, \
            self.host, \
            self.date_s, \
            self.date_e, \
            self.log_user, \
            self.version, \
            self.c_time, \
            self.token


class dealer(models.Model):
    dealer = models.CharField(max_length=6)
    mb = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=64, null=True)
    city = models.CharField(max_length=64, null=True)
    district = models.CharField(max_length=6, null=True)
    mobile = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=40, null=True)
    desc = models.CharField(max_length=256, null=True)
    date_s = models.IntegerField(default=0)
    date_e = models.IntegerField(default=0)

    def __unicode__(self):
        return self.dealer, \
            self.mb, \
            self.name, \
            self.city, \
            self.district, \
            self.mobile, \
            self.email, \
            self.desc, \
            self.date_s, \
            self.date_e


class Workorder(models.Model):
    # 用户表
    user = models.CharField(max_length=16)
    type = models.CharField(max_length=16)
    content = models.CharField(max_length=2048)
    img = models.ImageField(upload_to='img', null=True)
    status = models.CharField(max_length=16)
    c_time = models.IntegerField(default=0)

    def __unicode__(self):
        return self.id, \
            self.user, \
            self.type, \
            self.content, \
            self.status, \
            self.c_time


class Stable_Asset(models.Model):
    asset = models.CharField(max_length=10, primary_key=True)

    def __unicode__(self):
        return self.asset


class Symbol_Info(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    exchange = models.CharField(max_length=20)
    symbol = models.CharField(max_length=12)
    symbol_ori = models.CharField(max_length=12, null=True)
    baseAsset = models.CharField(max_length=20, null=True)
    quoteAsset = models.CharField(max_length=20, null=True)
    tickSize = models.IntegerField(default=2)  # 价格小数位
    minQty = models.IntegerField(default=8)    # 交易数量小数位
    minNotional = models.FloatField(default=0)  # 最小成交金额
    update_time = models.IntegerField(default=0)

    def __unicode__(self):
        return self.id, \
            self.exchange, \
            self.symbol, \
            self.symbol_ori, \
            self.baseAsset, \
            self.quoteAsset, \
            self.tickSize, \
            self.minQty, \
            self.minNotional, \
            self.update_time


class Symbol_Info2(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    exchange = models.CharField(max_length=20)
    t_type = models.CharField(max_length=12, default='t_spot')
    symbol = models.CharField(max_length=20)
    symbol_ori = models.CharField(max_length=20, null=True)
    baseAsset = models.CharField(max_length=20, null=True)
    quoteAsset = models.CharField(max_length=20, null=True)
    tickSize = models.IntegerField(default=2)  # 价格小数位
    minQty = models.IntegerField(default=8)    # 交易数量小数位
    minNotional = models.FloatField(default=0)  # 最小成交金额
    contract_val = models.FloatField(default=0)     # 合约面值
    listing = models.CharField(max_length=10, null=True)    # 合约上线日
    delivery = models.CharField(max_length=10, null=True)   # 合约交割日
    update_time = models.IntegerField(default=0)

    def __unicode__(self):
        return self.id, \
            self.exchange, \
            self.t_type, \
            self.symbol, \
            self.symbol_ori, \
            self.baseAsset, \
            self.quoteAsset, \
            self.tickSize, \
            self.minQty, \
            self.minNotional, \
            self.contract_val, \
            self.listing, \
            self.delivery, \
            self.update_time


class Ping(models.Model):
    user = models.CharField(max_length=16)
    host = models.CharField(max_length=16)
    timer = models.IntegerField(default=0)
    live = models.IntegerField(default=0)
    task = models.IntegerField(default=0)
    market = models.IntegerField(default=0)
    mem_pct = models.FloatField(default=0)
    cpu_pct = models.FloatField(default=0)

    def __unicode__(self):
        return self.user, \
            self.host, \
            self.timer, \
            self.live, \
            self.task, \
            self.market, \
            self.mem_pct, \
            self.cpu_pct


class Server_Monitor(models.Model):
    host = models.CharField(max_length=40, primary_key=True)
    live = models.IntegerField(default=0)
    gap = models.IntegerField(default=600)

    def __unicode__(self):
        return self.host, \
            self.live, \
            self.gap


class User_Opt_List(models.Model):
    user = models.CharField(max_length=16)
    exchange = models.CharField(max_length=20)
    account = models.CharField(max_length=20)
    t_type = models.CharField(max_length=12, default='t_spot')
    brief = models.CharField(max_length=2)
    symbol = models.CharField(max_length=20)
    symbol_ori = models.CharField(max_length=20, null=True)
    baseAsset = models.CharField(max_length=20, default='')
    quoteAsset = models.CharField(max_length=20, default='')
    top = models.IntegerField(default=0)
    marked = models.CharField(max_length=1, null=True)
    theLast = models.CharField(max_length=1, null=True)
    sequence = models.IntegerField(default=0)
    alert = models.IntegerField(default=0)
    alert_spec = models.IntegerField(default=0)
    alert_type = models.CharField(max_length=10, null=True)
    alert_value = models.IntegerField(default=0)
    tickSize = models.IntegerField(default=2)  # 价格小数位
    minQty = models.IntegerField(default=8)  # 交易数量小数位
    minNotional = models.FloatField(default=0)  # 最小成交金额
    contract_val = models.FloatField(default=0)  # 合约面值
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user, \
            self.exchange, \
            self.account, \
            self.t_type, \
            self.symbol, \
            self.symbol_ori, \
            self.baseAsset, \
            self.quoteAsset, \
            self.top, \
            self.marked, \
            self.theLast, \
            self.sequence, \
            self.alert, \
            self.alert_spec, \
            self.alert_type, \
            self.alert_value, \
            self.tickSize, \
            self.minQty, \
            self.minNotional, \
            self.contract_val, \
            self.order


class Symbol_Order(models.Model):
    exchange = models.CharField(max_length=20)
    t_type = models.CharField(max_length=12, default='t_spot')
    symbol = models.CharField(max_length=20)
    idx = models.IntegerField(default=0)
    price = models.CharField(max_length=16, default='0')
    q_price = models.CharField(max_length=16, default='0')
    symbol_ori = models.CharField(max_length=20, null=True)
    baseAsset = models.CharField(max_length=20, null=True)
    quoteAsset = models.CharField(max_length=20, null=True)
    tickSize = models.IntegerField(default=2)  # 价格小数位
    minQty = models.IntegerField(default=8)  # 交易数量小数位
    minNotional = models.FloatField(default=0)  # 最小成交金额

    def __unicode__(self):
        return self.exchange, \
            self.t_type, \
            self.symbol, \
            self.idx, \
            self.price, \
            self.q_price, \
            self.symbol_ori, \
            self.baseAsset, \
            self.quoteAsset, \
            self.tickSize, \
            self.minQty, \
            self.minNotional


class Symbol_Market(models.Model):
    exchange = models.CharField(max_length=20)
    t_type = models.CharField(max_length=12, default='t_spot')
    symbol = models.CharField(max_length=20)
    idx = models.IntegerField(default=0)
    server = models.CharField(max_length=64, null=True)

    def __unicode__(self):
        return self.exchange, \
            self.t_type, \
            self.symbol, \
            self.idx, \
            self.server


class User_Vol_Inbound(models.Model):
    UVIId = models.BigIntegerField(primary_key=True)
    UVIType = models.CharField(max_length=1)
    UVOId = models.BigIntegerField(null=True)
    user = models.CharField(max_length=16)
    host = models.CharField(max_length=16)
    docId = models.BigIntegerField(default=0)
    type = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    exchange = models.CharField(max_length=20)
    account = models.CharField(max_length=20)
    t_type = models.CharField(max_length=12, default='t_spot')
    symbol = models.CharField(max_length=20)
    ord_num = models.IntegerField(default=5)
    end_time = models.BigIntegerField(default=0)
    exe_qty = models.FloatField(default=0)
    exe_price = models.FloatField(default=0)
    exe_vol_u = models.FloatField(default=0)
    exe_vol = models.FloatField(default=0)
    exe_fee_u = models.FloatField(default=0)
    exe_fee = models.FloatField(default=0)
    quote_price = models.FloatField(default=0)
    fee_rate = models.FloatField(default=0)
    fee_price = models.FloatField(default=0)

    def __unicode__(self):
        return self.UVIId, \
            self.UVIType, \
            self.UVOId, \
            self.user, \
            self.host, \
            self.docId, \
            self.type, \
            self.status, \
            self.exchange, \
            self.account, \
            self.t_type, \
            self.symbol, \
            self.ord_num, \
            self.end_time, \
            self.exe_qty, \
            self.exe_price, \
            self.exe_vol, \
            self.exe_fee, \
            self.exe_fee_u, \
            self.quote_price, \
            self.fee_rate, \
            self.fee_price


class Symbol_flag(models.Model):
    exchange = models.CharField(max_length=20)
    symbol = models.CharField(max_length=20)
    margin = models.CharField(max_length=1, default='')

    def __unicode__(self):
        return self.exchange, \
            self.symbol, \
            self.margin


class Exchange_Account(models.Model):
    user = models.CharField(max_length=16)
    exchange = models.CharField(max_length=20)
    account = models.CharField(max_length=64)
    t_type = models.CharField(max_length=12, default='t_spot')
    acct_desc = models.CharField(max_length=64)
    key1 = models.CharField(max_length=256, null=True)
    key2 = models.CharField(max_length=256, null=True)
    key3 = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=1, default='A')

    def __unicode__(self):
        return self.user, \
            self.exchange, \
            self.account, \
            self.t_type, \
            self.acct_desc, \
            self.key1, \
            self.key2, \
            self.key3, \
            self.status


# class Calory_Binance(models.Model):
#     open_time = models.IntegerField(default=0)
#     symbol = models.CharField(max_length=20)
#     price = models.CharField(max_length=16, default='0')
#     p_b1m = models.CharField(max_length=16, default='0')
#     p_pct60 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
#     qty = models.CharField(max_length=16, default='0')
#     qty24 = models.CharField(max_length=16, default='0')
#     p_delta = models.DecimalField(max_digits=5, decimal_places=2, default=0)
#     q_delta = models.DecimalField(max_digits=5, decimal_places=2, default=0)
#     calory = models.DecimalField(max_digits=7, decimal_places=2, default=0)
#
#     def __unicode__(self):
#         return self.open_time, \
#                self.symbol, \
#                self.price, \
#                self.p_b1m, \
#                self.p_pct60, \
#                self.qty, \
#                self.qty24, \
#                self.calory, \
#                self.p_delta, \
#                self.q_delta
#
#
# class Calory_Huobi(models.Model):
#     open_time = models.IntegerField(default=0)
#     symbol = models.CharField(max_length=20)
#     price = models.CharField(max_length=16, default='0')
#     p_b1m = models.CharField(max_length=16, default='0')
#     p_pct60 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
#     qty = models.CharField(max_length=16, default='0')
#     qty24 = models.CharField(max_length=16, default='0')
#     p_delta = models.DecimalField(max_digits=5, decimal_places=2, default=0)
#     q_delta = models.DecimalField(max_digits=5, decimal_places=2, default=0)
#     calory = models.DecimalField(max_digits=7, decimal_places=2, default=0)
#
#     def __unicode__(self):
#         return self.open_time, \
#                self.symbol, \
#                self.price, \
#                self.p_b1m, \
#                self.p_pct60, \
#                self.qty, \
#                self.qty24, \
#                self.calory, \
#                self.p_delta, \
#                self.q_delta
#
# class Calory_Binance_8hours(models.Model):
#     calory_time = models.IntegerField(default=0)
#     symbol = models.CharField(max_length=20)
#     price = models.CharField(max_length=16, default='0')
#     p_pct60 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
#     qty = models.CharField(max_length=16, default='0')
#     qty24 = models.CharField(max_length=16, default='0')
#     calory = models.DecimalField(max_digits=7, decimal_places=2, default=0)
#
#     def __unicode__(self):
#         return self.calory_time, \
#                self.symbol, \
#                self.price, \
#                self.p_pct60, \
#                self.qty, \
#                self.qty24, \
#                self.calory
#
# class Calory_Huobi_8hours(models.Model):
#     calory_time = models.IntegerField(default=0)
#     symbol = models.CharField(max_length=20)
#     price = models.CharField(max_length=16, default='0')
#     p_pct60 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
#     qty = models.CharField(max_length=16, default='0')
#     qty24 = models.CharField(max_length=16, default='0')
#     calory = models.DecimalField(max_digits=7, decimal_places=2, default=0)
#
#     def __unicode__(self):
#         return self.calory_time, \
#                self.symbol, \
#                self.price, \
#                self.p_pct60, \
#                self.qty, \
#                self.qty24, \
#                self.calory
#

# class Kline(models.Model):
#     skey = models.CharField(max_length=40, primary_key=True)
#     open_time = models.IntegerField(default=0)
#     open = models.FloatField(default=0)
#     high = models.FloatField(default=0)
#     low = models.FloatField(default=0)
#     close = models.FloatField(default=0)
#     volumne = models.FloatField(default=0)
#     qvol = models.FloatField(default=0)
#
#     def __unicode__(self):
#         return self.skey, \
#                self.open_time, \
#                self.open, \
#                self.high, \
#                self.low, \
#                self.close, \
#                self.volumne, \
#                self.qvol
#
# class Kline_Binance(models.Model):
#     open_time = models.IntegerField(default=0, primary_key=True)
#     open = models.DecimalField(max_digits=11, decimal_places=10, default=0)
#     high = models.DecimalField(max_digits=11, decimal_places=10, default=0)
#     low = models.DecimalField(max_digits=11, decimal_places=10, default=0)
#     close = models.DecimalField(max_digits=11, decimal_places=10, default=0)
#     volumne = models.DecimalField(max_digits=16, decimal_places=10, default=0)
#     qvol = models.DecimalField(max_digits=16, decimal_places=10, default=0)
#
#     def __unicode__(self):
#         return self.open_time, \
#                self.open, \
#                self.high, \
#                self.low, \
#                self.close, \
#                self.volumne, \
#                self.qvol
