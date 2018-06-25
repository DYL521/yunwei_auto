#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  

## 演示继承之间的关系

class Bbh:
    def server(self):
        self.songz() ##slef,还是咱这个对象obj，所以又从头（子类）开始找！！！！

    def songz(self):
        print('宋--------1')

    def poress_request(self):
        print('yun')


class Mr(Bbh):

    def songz(self):
        print('宋--------2')  ## 5、执行这个方法！！！！顺序不能错

    def xiaowen(self):
        self.poress_request()

class A:
    def poress_request(self):
        print('yun')


class B(A,Mr): ## 多继承
    def poress_request(self):
        print('yun')

## self:无论在父类还是子类，都是只实例化的对象！！
## 若创建的是子类的实例，那么，父类和子类的self，都是指子类的self


obj = B()   ## 1
obj.server()## 2







