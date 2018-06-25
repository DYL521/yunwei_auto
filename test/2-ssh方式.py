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
    缺点：慢
    优点：无agent
'''
## 本例子基于paramiko
import requests
import paramiko
########## 1、获取未采集的主机名###########

#result1 = requests.get('htttp:www.127.0.0.1:8000/assstes.html') ## 未获取的主机名

# 假设  result1 = ['c1.com','c2.com'....]

##########2、通过paramiko连接远程服务器，执行命令 ###########

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.11.58.138', port=22, username='dyl', password='111111')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
result = stdout.read()
print(type(result)) ##<class 'bytes'>
#decode('utf-8')
print(result.decode('utf-8') ) ## 直接把bytes转成utf-8编码
# 关闭连接
ssh.close()

## 把中间机器执行的结果返回到API就可以了
data_dict = {result}

'''
    只要遍历未查询的主机名，就可以连接查询所有主机的信息
'''

'''
    本代码放在中间控制机器上就可以l
'''

