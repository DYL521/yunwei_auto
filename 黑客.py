#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @author: DYL  
 @contact: chng547835@163.com  
 """
import requests
host_data = {
    'status': True,
    'data': {
        'hostname': 'cl.com',
        'disk': {'status': 'True', 'data': 'xxxx'},
        'mem': {'status': 'True', 'data': 'xxxx'},
        'nic': {'status': 'True', 'data': 'xxxx'},
    }
}

response = requests.post(
    url='http://127.0.0.1:8000/api/asset/',  ##auth_keys 不接受？？
    headers={'auth-keys': '390656a644a7ae62d4ef8826a60a37bd|1530012800.7105415'},  ## 这里的key不能写_(下划线)（如：auth_keys），对方貌似不接受
    # params={'k1': 123, 'k2': 456},  ##URL中
    # data=host_data, ##请求体中
    json=host_data,  ## 数据在request.body中
)
print(response.text)

