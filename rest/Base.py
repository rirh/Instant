# -*- coding: utf-8 -*-
from datetime import datetime
from time import time
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer


class Timer:
    # args前面加一颗*是元祖 两颗*是字典
    def __init__(self):
        # super().__init__()
        self.iso = datetime.now()
        self.epoch = time()


class TimerSerializer(serializers.Serializer):
    iso = serializers.DateTimeField()
    epoch = serializers.FloatField()


