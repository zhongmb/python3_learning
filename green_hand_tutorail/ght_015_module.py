#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Python3 模块
    1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
    2、sys.argv 是一个包含命令行参数的列表。
    3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
    一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。

    from…import 语句
        Python的from语句让你从模块中导入一个指定的部分到当前命名空间中
    From…import* 语句
        把一个模块的所有内容全都导入到当前的命名空间也是可行的
    __name__属性
        一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，
        我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
    dir() 函数
        内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
    包
        包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
    从一个包中导入*
        导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，
        那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
        作为包的作者，可别忘了在更新包之后保证 __all__ 也更新了啊。
    属性__path__
        这是一个目录列表，里面每一个包含的目录都有为这个包服务的__init__.py，
        你得在其他__init__.py被执行前定义哦。可以修改这个变量，用来影响包含在包里面的模块和子包。
'''

import sys
import datetime

def main(argv):
    '''主函数'''
    print("运行参数", argv)
    print(__doc__)
    print(datetime.datetime(2017, 5, 24))


if __name__ == "__main__":
    main(sys.argv)
