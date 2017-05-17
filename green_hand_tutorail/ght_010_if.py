#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Python3 条件控制
    if 语句
        Python中if语句的一般形式如下所示：
            if condition_1:
                statement_block_1
            elif condition_2:
                statement_block_2
            else:
                statement_block_3
        Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
    注意：
        1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。
        2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
        3、在Python中没有switch – case语句。
    以下为if中常用的操作运算符:
        操作符	描述
        <	小于
        <=	小于或等于
        >	大于
        >=	大于或等于
        ==	等于，比较对象是否相等
        !=	不等于
    if 嵌套
        在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。

'''

import sys

def main(argv):
    '''主函数'''
    print("运行参数", argv)
    print(__doc__)
    if __name__ == "__main__":
        print("运行模块")
    else:
        print("导入模块方式运行")


if __name__ == "__main__":
    main(sys.argv)
