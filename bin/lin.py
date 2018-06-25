#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  


## 方式1： 单独的package文件
# ## 只放置可执行文件
# from src import package
# ## 打包数据
# data_dict =  package.pack()


## 方式2：
## 放在__init__.py文件

# from src import plugins  ##导入文件夹，默认导入__init__,并且自动执行__init__
#
# plugins.pack()
#
# '''
#     所以，导入一个py文件：from src.plugins import pack 只会加载相应的文件
#     导入一个文件夹（或者包，模块、类库），会加载文件下的__init__.py文件
# '''


from src.script import run

if __name__ == '__main__':
    run()