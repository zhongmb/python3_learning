#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Python3 函数
    定义一个函数
        return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
    可更改(mutable)与不可更改(immutable)对象
        在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
        不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，
            而 5 被丢弃，不是改变a的值，相当于新生成了a。
        可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，
            本身la没有动，只是其内部的一部分值被修改了。
        参数,以下是调用函数时可使用的正式参数类型：
            必需参数
                必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
            关键字参数
                关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
                使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
            默认参数
                调用函数时，如果没有传递参数，则会使用默认参数。
            不定长参数
                加了星号（*）的变量名会存放所有未命名的变量参数。
        匿名函数:使用 lambda 来创建匿名函数。
            所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
            lambda 只是一个表达式，函数体比 def 简单很多。
            lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
            lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
            虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，
                后者的目的是调用小函数时不占用栈内存从而增加运行效率。
            语法
                lambda 函数的语法只包含一个语句，如下：
                lambda [arg1 [,arg2,.....argn]]:expression
        return语句
            return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None
        变量作用域
            Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
            变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4中，分别是：
            L （Local） 局部作用域
            E （Enclosing） 闭包函数外的函数中
            G （Global） 全局作用域
            B （Built-in） 内建作用域
            以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），
                再找不到就会去全局找，再者去内建中找。
        重要***********:
            Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
            其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
            也就是说这这些语句内定义的变量，外部也可以访问
                实例中 msg 变量定义在 if 语句块中，但外部还是可以访问的。
                    if True:
                        msg = 'I am from Runoob'
                    print(msg)
                如果将 msg 定义在函数中，则它就是局部变量，外部不能访问：
        global 和 nonlocal关键字
            当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。

'''

import sys

NUM = 2
def fun1():
    '''global使用实例, 需要使用 global 关键字声明'''
    global NUM #这种用法会报警
    print(NUM)
    NUM = 123
    print(NUM)

def outer():
    '''nonlocal使用实例'''
    num = 10
    def inner():
        '''闭包内部函数'''
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)

def main(argv):
    '''主函数'''
    print("运行参数", argv)
    print(__doc__)
    fun1()
    outer()

if __name__ == "__main__":
    main(sys.argv)
