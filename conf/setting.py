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