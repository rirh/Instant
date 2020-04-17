##### 微信加密货币交易所

##### Start  server local

```python
python3 manage.py runserver
```

##### Start  server cloud

```python
# 启动 uwsgi --ini uwsgi.ini 
# 停止 uwsgi --stop uwsgi.pid
# 重启 uwsgi --reload uwsgi.pid 
```

##### django cmd

```python
# 进入项目交互的命令行 python manage.py shell
# 启动服务 python3 manage.py runserver
# 重启 uwsgi --reload uwsgi.pid 
```



1. 服务端部署项目

   ```
   target：
   正常访问 https://crypto.huzhihui.org.cn/ 
   done!
   ```

   

2. RESTFULL接口

   ```
   target:
   货币列表的增删改查
   文件上传
   图片静态资源访问
   ```

3. mysql操作

   ```
   target:
   货币的增删改查
   ```

4. redis缓存操作

   ```
   target:
   查询时先到redis中查询，没有找到数据在进行数据库查询。提高运行速度
   ```

5. django 

   ```
   target:
   理解model
   理解view
   开发前后端分离和不不分离demo
   学习admin的配置和使用

   ```
6. 静态文件配置

   ```
   target:
   配置静态文件访问

   ```

   

   