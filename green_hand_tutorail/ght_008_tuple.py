#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Python3 元组
    Python 的元组与列表类似，不同之处在于元组的元素不能修改。
    元组使用小括号，列表使用方括号。
    元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
    创建空元组
        tup1 = ();
    元组中只包含一个元素时，需要在元素后面添加逗号
        tup1 = (50,);
    修改元组
        元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
    删除元组
        元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
'''

import sys

def main(argv):
    '''主函数'''
    print("运行参数", argv)
    print(__doc__)
    tup1 = ()
    tup2 = (50,)
    print(tup1, tup2)


if __name__ == "__main__":
    main(sys.argv)
