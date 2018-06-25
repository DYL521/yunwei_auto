#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """
# 1、安装Saltstack
#http://docs.saltstack.cn/topics/installation/rhel.html

## centos7： rpm --import https://repo.saltstack.com/yum/redhat/7/x86_64/latest/SALTSTACK-GPG-KEY.pub
##          安装master --- 中间机器： yum install salt-master
##          安装Slave  ----客户端机器：yum install salt-minion

## 这里演示用cenos7 --- 主机、丛机都是本机
'''
    Master:
        a、配置文件，监听IP
           vim /etc/salt/master  
           把 Interface：改成本机的ip地址
        b、启动master
            systemctl enable salt-master.service
    Slave：
        a、配置文件，连接哪个master
            vim /etc/salt/minion
            master：修改 --- 远程master地址 如：10.11.58.138
        b、启动sale
            systemctl start salt-minion.service
'''


## 创建关系
'''
## 1、查看都有哪些人来连接
#     salt-key -L

    Accepted Keys: 接受的
    Denied Keys: # 拒接的
    Unaccepted Keys: 未接受的
        c1.com
        c2.com
        c3.com
    Rejected Keys:

## 2、主机接受连接
   Master ： salt-key -a c1.com     ## 接受c1.com的连接
    
    3、执行命令-- 向slave发送命令执行
        master：   salt 'c2.salt.com' cmd.run  'ifconfig'
'''



''' 
    Master：执行代码
    Saltstack -- 是python写的
    
    Salt 是一个py文件 --- /usr/bin/salt
    自己执行代码
    
    ## 测试代码
    import salt.client
    local = salt.client.LocalClient()
    result = local.cmd('c2.salt.com', 'cmd.run', ['ifconfig'])
    ##result 是一个字典，vaues是返回的结果
    
'''


################CMDB执行的事儿#########################

#result1 = requests.get('htttp:www.127.0.0.1:8000/assstes.html') ## 未获取的主机名

# 假设  result1 = ['c1.com','c2.com'....]

################连接远程服务器（Master）执行命令#########################

## 方式1：拿到字符串
import subprocess
subprocess.getoutput(" salt 'c2.salt.com' cmd.run  'ifconfig'") ## 给远程master执行，master再去salve取数据

## 方式2：拿到字典
import salt.client
local = salt.client.LocalClient()
result = local.cmd('c2.salt.com', 'cmd.run', ['ifconfig'])
##result 是一个字典，vaues是返回的结果

## 发送数据到API
import requests
requests.post('htttp:www.127.0.0.1:8000/assstes.html',data= data_dict)




