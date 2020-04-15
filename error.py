#!/usr/bin/python3

# try:
#     text = input('Enter something --> ')
# except EOFError:
#     print('Why did you do an EOF on me?')
# except KeyboardInterrupt:
#     print('You cancelled the operation.')
# else:
#     print('You entered {}'.format(text))
# import redis
# r = redis.StrictRedis(host='0.0.0.0', port=6379)
# r.set('age', '20')
# print(r.get('age'))


# def integrate_f(a, b, N):
#     s = 0
#     dx = (b-a) / N
#     for i in range(N):
#         s += 2.71828182846**(-(a+i*dx)**2)
#     return s*dx


# if __name__ == "__main__":
#     a= integrate_f(1.0, 10.0, 100000000)
#     print(a)

# import pymysql

# 打开数据库连接
# db = pymysql.connect("localhost", "root", "", "")

# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# 创建数据库
# cursor.execute("""CREATE DATABASE IF NOT EXISTS CRYPTO""")
# cursor.execute("DROP TABLE IF EXISTS CRYPTO")
# 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""

# cursor.execute(sql)
# SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 如果发生错误则回滚
#     db.rollback()
# db.close()
# print(__name__)