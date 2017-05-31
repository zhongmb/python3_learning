#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Python3 错误和异常
    语法错误
        Python 的语法错误或者称之为解析错  SyntaxError: invalid syntax
    异常
        即便Python程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
        大多数的异常都不会被程序处理，都以错误信息的形式展现在这里
    异常处理
        以下例子中，让用户输入一个合法的整数，但是允许用户中断这个程序（使用 Control-C 或者操作系统提供的方法）。
            用户中断的信息会引发一个 KeyboardInterrupt 异常。
    格式:
        try:
            .....
        except ValueError as er:
            ......
        except (RuntimeError, TypeError, NameError):
            ......
        except :
            print("Unexpected error:", sys.exc_info()[0])
            raise
        else:
            ......
    抛出异常
        Python 使用 raise 语句抛出一个指定的异常。
    用户自定义异常
        你可以通过创建一个新的exception类来拥有自己的异常。
        异常应该继承自 Exception 类，或者直接继承，或者间接继承，
    定义清理行为finally
        try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。
        不管try子句里面有没有发生异常，finally子句都会执行。
        如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，
        而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后再次被抛出。
    预定义的清理行为
        一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，
        那么这个标准的清理行为就会执行。
        关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法

'''

import sys

def main(argv):
    '''主函数'''
    print("运行参数", argv)
    print(__doc__)
    with open("myfile.txt") as file_obj:
        for line in file_obj:
            print(line, end="")


if __name__ == "__main__":
    main(sys.argv)
