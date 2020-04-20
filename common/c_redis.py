import redis

# try:
# host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
r.set('name', 'junxi')  # key是"foo" value是"bar" 将键值对存入redis缓存
print(r['name'])
print(r.get('name'))  # 取出键name对应的值
print(type(r.get('name')))
# except Exception:
#     print('''error''')
#     pass
