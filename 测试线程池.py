#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @author: DYL  
 @contact: chng547835@163.com  
 """
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time
## 创建线程池
pool = ThreadPoolExecutor(5)
#pool = ProcessLookupError(5) ## 进程池创建  --- 他们非常相似

def task(arg):
    print(arg)
    time.sleep(1)

for i in range(50):
    pool.submit(task,i) ## task 函数名， i 是函数的参数

'''
    python2中没有线程池，python3才有线程池
    python2中只有进程池，python有进程池和线程池
'''