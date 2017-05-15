'''
    只是python基础语法
'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

def info():
    '''
    编码
        默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：
        # -*- coding: cp-1252 -*-

    标识符
        第一个字符必须是字母表中字母或下划线'_'。
        标识符的其他的部分有字母、数字和下划线组成。
        标识符对大小写敏感。
        在Python 3中，非-ASCII 标识符也是允许的了。
    python保留字
        保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：

    注释
        Python中单行注释以 # 开头，
        多行注释可以用多个 # 号,每一行一个
    行与缩进
        python最具特色的就是使用缩进来表示代码块，不需要使用大括号({})。
        缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
    多行语句
        Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\\)来实现多行语句
        在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\\)
    数据类型
        python中数有四种类型：整数、长整数、浮点数和复数。
            整数， 如 1
            长整数 是比较大的整数
            浮点数 如 1.23、3E-2
            复数 如 1 + 2j、 1.1 + 2.2j
    字符串
        python中单引号和双引号使用完全相同。
        使用三引号(\'\'\'或\"\"\")可以指定一个多行字符串。
        转义符 \'\\\'
        自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \\n" 则\\n会显示，并不是换行。
        python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
        字符串是不可变的。
        按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
    空行
        函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。
        类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
        空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。
        但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
        记住：空行也是程序代码的一部分。

    等待用户输入input(提示字符串)
        执行下面的程序在按回车键后就会等待用户输入：

    同一行显示多条语句
        Python可以在同一行中使用多条语句，语句之间使用分号(;)分割

    多个语句构成代码组
        缩进相同的一组语句构成一个代码块，我们称之代码组。
        像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
        我们将首行及后面的代码组称为一个子句(clause)。

    Print 输出
        print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""

    import 与 from...import
        在 python 用 import 或者 from...import 来导入相应的模块。
        将整个模块(somemodule)导入，格式为： import somemodule
        从某个模块中导入某个函数,格式为： from somemodule import somefunction
        从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
        将某个模块中的全部函数导入，格式为： from somemodule import *

    python命令行：可以采用python -h来查看；python -c
        -c cmd : 执行一个字符串命令，例如：python -c "print('234+456=',234+456)"
        -m mod : 把一个库模块作为脚本运行，例如：pip与python -m pip 作用相等

    help() 函数
        调用 python 的 help() 函数可以打印输出一个函数的文档字符串


    '''
    print(info.__doc__)

def identifier_def():
    '''
        标识定义,可以使用中文字符作为变量名
        性别 = "男"
        体重 = 69
        print(_age, 体重, 性别)
    '''
    _age = 12
    print(_age)

def system_keyword():
    '''
        获取系统保留关键字
    '''
    import keyword
    print(keyword.kwlist)

def input_print():
    '''
        输入输出函数
    '''

    age = input("请输入你的年龄:")
    name = input("请输入你的姓名:")
    print("你的年龄和姓名分别是:", age, end=' ')
    print(name)

def used_help():
    '''
        help使用
    '''
    help(max)

def main(argv):
    '''
    主函数
    '''
    print("运行参数", argv)
    info()
    identifier_def()
    system_keyword()
    input_print()
    used_help()

if __name__ == "__main__":
    main(sys.argv)
