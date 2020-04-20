import pymysql
from django.db import models

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '',
    'db': 'crypto'
}


class Sql:
    def __init__(self):
        super().__init__()
        self.conn = pymysql.connect(
            host=config.host, port=config.port, user=config.user, passwd=config.passwd, db=config.db)
        
