#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """
## 配置文件

MODE = "Agent" ## ssh 、Salt 三种


# plugins
PIUGINS = {
    'disk':'src.plugins.disk.DiskPlugin',
    'men':'src.plugins.men.MemPlugin',
    'nic':'src.plugins.nic.NicPlugin'
}
## 服务器没有唯一的标识：
## 所以得，指定规则，标识主机=====

'''
mac 地址、sn（主板号）都不能是唯一标识的。。。因为还有虚拟机
    虚拟机sn号是一样的 
    1、如果没有虚拟机,就可以是sn号：
    2、有公司，认为虚拟机不是资产，宿主机才是资产！！
    3、宿主机和虚拟机都是资产--用规则来标识，但是如果文件内容被修改，也会出错
'''

## 制定规则，主机名不能重复 -原则上原则上不能改！！
## 即使文件名改了，也不能影响CMDB -- 但是文件里面改名了，真是没办法

## 重装系统：主机名 --必须指定，物理机虚拟机名字得确定
