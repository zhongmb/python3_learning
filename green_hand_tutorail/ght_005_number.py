#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Python3 数字(Number)
    Python 数字数据类型用于存储数值。
    数据类型是不允许改变的,这就意味着如果改变数字数据类型得值，将重新分配内存空间。
Python 数字运算
    在整数除法中，除法（/）总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 //
    在交互模式中，最后被输出的表达式结果被赋值给变量 _
数学函数
    函数	返回值 ( 描述 )
    abs(x)	返回数字的绝对值，如abs(-10) 返回 10
    ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
    cmp(x, y)
    如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用 使用 (x>y)-(x<y) 替换。
    exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
    fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
    floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
    log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
    log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
    max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
    min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
    modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
    pow(x, y)	x**y 运算后的值。
    round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
    sqrt(x)	返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j
随机数函数
    choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
    randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
    random()	随机生成下一个实数，它在[0,1)范围内。
    seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
    shuffle(lst)	将序列的所有元素随机排序
    uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
三角函数
    函数	描述
    acos(x)	返回x的反余弦弧度值。
    asin(x)	返回x的反正弦弧度值。
    atan(x)	返回x的反正切弧度值。
    atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
    cos(x)	返回x的弧度的余弦值。
    hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
    sin(x)	返回的x弧度的正弦值。
    tan(x)	返回x弧度的正切值。
    degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
    radians(x)	将角度转换为弧度
数学常量
    常量	描述
    pi	数学常量 pi（圆周率，一般以π来表示）
    e	数学常量 e，e即自然常数（自然常数）。
'''

import sys

def print_buildins():
    '''打印内建函数'''
    for in_func in dir(__builtins__):
        print(in_func)

def main(argv):
    '''主函数'''
    print("运行参数", argv)
    print(__doc__)
    print_buildins()

if __name__ == "__main__":
    main(sys.argv)
