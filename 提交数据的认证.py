#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @author: DYL  
 @contact: chng547835@163.com  
 """
import requests
import hashlib
import time

## 当前时间
current_time = time.time()
## 密码名文
app_id = 'adsddaqweqeq'
## 当前时间组成一个字符串
app_id_time = '%s|%s' % (app_id, current_time)

## MD5-加密
m = hashlib.md5()
m.update(bytes(app_id_time, encoding='utf-8'))  ## 变成字节，并且编码成utf-8
authkey = m.hexdigest()
print(authkey)

## 把时间也带上
authkey_time = "%s|%s" % (authkey, current_time)
###a3bf975294b1321b88bfe70fba636fa7|1530009425.5828853
print(authkey_time)

## 假设是获取的主机信息 ，现在把这个数据提交到API
host_data = {
    'status': True,
    'data': {
        'hostname': 'cl.com',
        'disk': {'status': 'True', 'data': 'xxxx'},
        'mem': {'status': 'True', 'data': 'xxxx'},
        'nic': {'status': 'True', 'data': 'xxxx'},
    }
}

### 数据提交 -- GET
# requests.get(
#     url='http://127.0.0.1:8000/api/asset/?key1=123',
#     # data=host_data,
# )
# requests.get(
#     url='http://127.0.0.1:8000/api/asset/',
#     params={'k1':123,'k2':456}
# )

### 数据提交 -- POST
### Forbidden (CSRF cookie not set.): /api/asset/
'''
    这里post提交时，会产生csrf错误，我们解决的办法是，关闭接收端函数的csrf
'''
## response ：拿到返回所有值
response = requests.post(
    url='http://127.0.0.1:8000/api/asset/',  ##auth_keys 不接受？？
    headers={'auth-keys': authkey_time},  ## 这里的key不能写_(下划线)（如：auth_keys），对方貌似不接受
    # params={'k1': 123, 'k2': 456},  ##URL中
    # data=host_data, ##请求体中
    json=host_data,  ## 数据在request.body中
    ## 请求头存放加密信息,不带这个信息，对方不接受!!
    ## 在请求头，请求体，都可以携带加密的参数
)
## 得到返回信息
print(response.text)

##请求体中 :<QueryDict: {'status': ['True'], 'data': ['hostname', 'disk', 'mem', 'nic']}>
##URL中 <QueryDict: {'k1': ['123'], 'k2': ['456']}>


'''
    GET:发送数据在URL中，没有请求体 
    POST：发送数据可以在URL中，也可以在请求体中
'''
