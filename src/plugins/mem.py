#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """
from .base import BasePlugin
## 内存
class MemPlugin(BasePlugin):

    def windows(self):
        output = self.shell_cmd('zzzzz')  ## 内部判断模式
        return output

    def linux(self):  ## 被重写了
        output = self.shell_cmd('aaaa')  ## 内部判断模式
        return output