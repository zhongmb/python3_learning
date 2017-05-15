#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

def info():
    '''
    Python3 基本数据类型
        Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
        在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
        等号（=）用来给变量赋值。
        等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。
    多个变量赋值
        Python允许你同时为多个变量赋值。例如：
            a = b = c = 1
            以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。
        您也可以为多个对象指定多个变量。例如：
            a, b, c = 1, 2, "runoob"
            以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。
    标准数据类型，Python3 中有六个标准的数据类型：
        Number（数字）
        String（字符串）
        List（列表）
        Tuple（元组）
        Sets（集合）
        Dictionary（字典）
    Number（数字）
        Python3 支持 int、float、bool、complex（复数）。
        在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
        内置的 type() 函数可以用来查询变量所指的对象类型。
        isinstance 和 type 的区别在于：type()不会认为子类是一种父类类型。isinstance()会认为子类是一种父类类型。
        注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
            到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
        您也可以使用del语句删除一些对象引用。
            del语句的语法是：
                del var1[,var2[,var3[....,varN]]]]
        数值运算
            1、Python可以同时为多个变量赋值，如a, b = 1, 2。
            2、一个变量可以通过赋值指向不同类型的对象。
            3、数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
            4、在混合计算时，Python会把整型转换成为浮点数。

    '''
    print(info.__doc__)

def test():
    counter = 100 # 整型变量 
    miles = 1000.0 # 浮点型变量 
    name = "runoob" # 字符串 
    print (counter) 
    print (miles) 
    print (name)



def main(argv):
    info()
    test()



if __name__ == "__main__":
    main(sys.argv)

