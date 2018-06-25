#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """
'''
    缺点：有Agent
    优点：
'''

## 1、采集数据
''' 不能用os，os没有返回值'''
import subprocess
import requests ## 发送请求

result =  subprocess.getoutput('ipconfig')
## result 进行正则匹配，获取想要的数据
print(result)

## 2、整理资产信息
data_dict = {
    'nic',{},
    'disk',{},
    'mem',{}

}

## 发送数据到API
requests.post('htttp:www.127.0.0.1:8000/assstes.html',data= data_dict)


'''
本代码放在每一台主机上
'''




