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
class BasePlugin(object):

    def __init__(self):  ## 验证配置文件
        mode_list = ['SSH', 'Salt', 'Agent']
        if setting.MODE in mode_list:
            self.mode = setting.MODE  ## 模式
        else:
            raise Exception('配置文件出错')

    def ssh(self, cmd):  ## paramiko 实现
        pass

    def agent(self, cmd):  ##subprocess 实现
        pass

    def salt(self, cmd):  ##Saltstack 实现
        pass

    def shell_cmd(self, cmd):
        '''
            判断当前的模式，并且执行对应的命令
        :param cmd: 命令
        :return: 返回结果
        '''
        if self.mode == 'SSH':
            ret = self.ssh(cmd)
        elif self.mode == 'Salt':
            ret = self.salt(cmd)
        else:
            ret = self.agent(cmd)  ###??
        return ret

    def execute(self):
        ret = self.shell_cmd('查看品台的命令')  ## 内部进行判断

        if ret == 'win':
            return self.windows()  ## 直接返回
        elif ret == 'Linux':
            return self.linux()
        else:
            raise Exception('只支持linux和window')

    def linux(self):
        raise Exception('...........')  ## 主动抛出异常，报错了

    def windows(self):
        raise Exception('...........')  ## 主动抛出异常，报错了


