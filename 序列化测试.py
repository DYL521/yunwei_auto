#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @author: DYL  
 @contact: chng547835@163.com  
 """
import time
import json
from datetime import date
from datetime import datetime

class Response():
    def __init__(self):
        self.status = True
        self.data = datetime.now()

data = {
    'k1':123,
    'k2':datetime.now(), ## datatime不能直接被序列化
    'k3':Response(),   ## 不能直接被初始化
}
'''
原生的json，只能序列化列表、字典等基本数据类型，其他对象或者数据类型都不可以序列化
若是要修改，必须特殊处理！！
'''
class JsonCustomEncoder(json.JSONEncoder):

    def default(self, field):
        #print(field)
        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field, date):
            return field.strftime('%Y-%m-%d')
        elif isinstance(field,Response):
            return field.__dict__ ## 字典，把对象的字段直接变成字典！！
        else:
            return json.JSONEncoder.default(self, field) ## 默认的序列化方式


## cls: 指定序列化其他类型的对象 -- 基本数据类型以外的数据类型
ds = json.dumps(data, cls=JsonCustomEncoder)
print(ds)