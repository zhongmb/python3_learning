#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Python3 循环语句
    Python中的循环语句有 for 和 while。
    同样需要注意冒号和缩进。另外，在Python中没有do..while循环。
    无限循环
        我们可以通过设置条件表达式永远不为 false 来实现无限循环
        你可以使用 CTRL+C 来退出当前的无限循环。
        无限循环在服务器上客户端的实时请求非常有用。
    while 循环使用 else 语句
    简单语句组
        类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
    range()函数
        如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
    break和continue语句及循环中的else子句
        break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
'''

import sys

def find_prime_number(max_number):
    '''查找质数'''
    print(2, '是质数')
    for check_num in range(3, max_number, 2):
        for factor_num in range(3, check_num, 2):
            if check_num % factor_num == 0:
                print(check_num, '等于', factor_num, '*', check_num // factor_num)
                break
        else:
            # 循环中没有找到元素
            print(check_num, '是质数')

def main(argv):
    '''主函数'''
    print("运行参数", argv)
    print(__doc__)
    find_prime_number(100)


if __name__ == "__main__":
    main(sys.argv)
