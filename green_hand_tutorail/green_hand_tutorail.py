#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
工程主文件
'''

import sys

def my_unkown():
    '''
    2_1.Python 的标准库提供了一个 keyword 模块,kwlist
    2_2.from somemodule import firstfunc
    3_1.isinstance与type的区别
    3_2.数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
    3_3.repr(x)将对象 x 转换为表达式字符串
    3_4.eval(str)用来计算在字符串中的有效Python表达式,并返回一个对象

    '''
    print(my_unkown.__doc__)

def main(argv):
    '''
    主函数
    '''
    print("运行参数", argv)
    my_unkown()


if __name__ == "__main__":
    main(sys.argv)
