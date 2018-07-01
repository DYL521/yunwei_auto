#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  



## agent 形式
# 1、采集资产
# 2、post发送API，并且存储到数据库等等


## SSH形式
# 1、获取今天未采集的主机列表
# 2、采集资产
# 3、将资产数据发送的API（POST）

## Salt形式
# 1、获取今天未采集的主机列表
# 2、采集资产
# 3、将资产数据发送的API（POST）


class BaseClient():

    def send_data(self, data_dict):
        pass


## 中间类
class SBaseClient():
    def get_host(self):
        ## 获取主机名
        host_list = []
        return host_list





class Agent(BaseClient): ## 只有senddata功能

    ## 本地文件
    def file_host(self):
        f = open('nid')
        data = f.read()
        f.close()
        if data: ## 有数据
            return data


    def process(self):
        ## 1、采集资产
        from .plugins import pack
        data_dict = pack()
        hostname = self.file_host()
        if hostname:
            data_dict['hostname'] = hostname
        else: ## 本地无nid文件
            # 获取当前的主机名
            # 写入nid 文件
            data_dict['hostname'] = 'aaaaaa'
        ## 2、将数据发送到API
        self.send_data(data_dict)

class SSH(SBaseClient):# 不仅有senddata还有get_host
    def process(self):
        ## 1、获取今日未采集的主机名
        host_list = self.get_host()
        for host in host_list:
            ## 2、采集资产
            data_dict = {}
            ## 3、将数据发送到API
            self.send_data(data_dict)

class Salt(SBaseClient):#不仅有senddata还有get_host
    def process(self):
        ## 1、获取今日未采集的主机名
        host_list = self.get_host()
        for host in host_list:
            ## 2、采集资产
            data_dict = {}
            ## 3、将数据发送到API
            self.send_data(data_dict)