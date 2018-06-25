#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """

## src  - 存放业务逻辑

## 采集资产，以三种不同的形式

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


## 硬盘
class DiskPlugin(BasePlugin):

    def windows(self):
        output = self.shell_cmd('ipconfig')  ## 内部判断模式
        return output ## 得到的是字符串

    def linux(self):  ## 被重写了
        output = self.shell_cmd('ifconfig')  ## 内部判断模式
        return output


## 内存
class MemPlugin(BasePlugin):

    def windows(self):
        output = self.shell_cmd('zzzzz')  ## 内部判断模式
        return output

    def linux(self):  ## 被重写了
        output = self.shell_cmd('aaaa')  ## 内部判断模式
        return output



obj = DiskPlugin()

result = obj.execute()  ## 执行父类的 ----- 每次找都从子类开始

## __init__（父类的） 、execute（父类的） 、linux（子类的，被重写）

### 可插拔式，插件！！
