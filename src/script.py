#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """
from conf import setting
from . import client


def run():
    ## 判断模式
    if setting.MODE == 'Agent':
        client.Agent().process()
    elif setting.MODE == 'SSH':
        client.SSH().process()
    elif setting.MODE == 'Salt':
        client.Salt().process()
    else:
        raise Exception('配置文件模式错误')
