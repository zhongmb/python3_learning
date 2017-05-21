#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Python3 迭代器与生成器
    迭代器
        迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
        迭代器是一个可以记住遍历的位置的对象。
        迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
        迭代器有两个基本的方法：iter() 和 next()。
        字符串，列表或元组对象都可用于创建迭代器
    生成器
        在 Python 中，使用了 yield 的函数被称为生成器（generator）。
        跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
        在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。
            并在下一次执行 next()方法时从当前位置继续运行。
        以下实例使用 yield 实现斐波那契数列：

'''

import sys

def fibonacci(count_num):
    '''生成器函数 - 斐波那契'''
    first, second, counter = 0, 1, 0
    while True:
        if counter > count_num:
            return
        yield first
        first, second = second, first + second
        counter += 1


def test_fibonacci():
    '''测试fibonacci'''
    iter_f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

    while True:
        try:
            print(next(iter_f), end=" ")
        except StopIteration:
            print("")
            return

def main(argv):
    '''主函数'''
    print("运行参数", argv)
    print(__doc__)
    test_fibonacci()


if __name__ == "__main__":
    main(sys.argv)
