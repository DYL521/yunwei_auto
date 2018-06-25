#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """

# from .plugins.disk import DiskPlugin
# from .plugins.mem import MemPlugin
# from .plugins.nic import NicPlugin

from conf import setting


def pack():
    # obj1 = DiskPlugin()
    # disk_info = obj1.execute()
    #
    # obj2 = MemPlugin()
    # mem_info = obj2.execute()
    #
    # obj3 = NicPlugin()
    # nic_info = obj3.execute()
    #
    # response={
    #     'nic':nic_info,
    #     'mem':mem_info,
    #     'disk':disk_info,
    # }
    '''
    PIUGINS = {
        'disk': 'src.plugins.disk.DiskPlugin',
        'men': 'src.plugins.men.MemPlugin',
        'nic': 'src.plugins.nic.NicPlugin'
    }
    '''
    response = {}
    for k, v in setting.PIUGINS.items():
        # ## v = 'src.plugins.disk.DiskPlugin', 字符串
        # ## 用反射实现
        # import importlib
        # m = importlib.import_module('src.plugins.disk') # 表示导入这个py文件
        # cls = getattr(m,'DiskPlugin')
        # # content = cls().execute() ##cls() 表示创建对象
        # # #相当于 from src.plugins import disk
        # # # content = disk.DiskPlugin().execute()

        import importlib
        m_path, classname = v.rsplit('.', maxsplit=1)  ## 只右边分隔后面的点
        m = importlib.import_module(m_path)  # 表示导入这个py文件
        cls = getattr(m, classname)
        response[k] = cls().execute()
    return response


'''
    为啥开发CMDB（运维自动化）？ -- 全部自动化
    1、资产管理 -- （基础条件）excel--手动填写（自动汇报，还有变更记录）
        采集数据四种方案：
            1、agent ：subprocess 定时提交到API -- 入库
            2、ssh ：paramiko 中控： 远程连接  速度比较慢
            3、saltStack ：依赖 Saltstack软件 -- 
            4、-----暂时不学urby
        API --- 中控机、或者直接是agent Master  --->
        
        
     --  全部自动化：
        自动装机、自动监控、自动初始化环境、自动发布部署、等等
     --- 自动化的基础是资产管理

'''
