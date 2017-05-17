#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Python3 字典
    字典是另一种可变容器模型，且可存储任意类型对象。
    字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
    键必须是唯一的，但值则不必。
    值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
    删除字典元素
        清空字典，清空(clear)只需一项操作。
        显示删除一个字典用del命令,也能删单一的元素
    字典键的特性
        字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
        两个重要的点需要记住：
        1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
        2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
    Python字典包含了以下内置方法：
        序号	函数及描述
        1	radiansdict.clear()        删除字典内所有元素
        2	radiansdict.copy()         返回一个字典的浅复制
        3	radiansdict.fromkeys()     创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
        4	radiansdict.get(key, default=None)  返回指定键的值，如果值不在字典中返回default值
        5	key in dict      如果键在字典dict里返回true，否则返回false
        6	radiansdict.items()    以列表返回可遍历的(键, 值) 元组数组
        7	radiansdict.keys()     以列表返回一个字典所有的键
        8	radiansdict.setdefault(key, default=None)
                和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
        9	radiansdict.update(dict2)    把字典dict2的键/值对更新到dict里
        10	radiansdict.values()         以列表返回字典中的所有值

'''

import sys

def loop_dict():
    '''遍历字典'''
    people_info = {"name" : "小明", "age" : 18}
    for name, value in people_info:
        print(name, value)

def main(argv):
    '''主函数'''
    print("运行参数", argv)
    print(__doc__)
    loop_dict()

if __name__ == "__main__":
    main(sys.argv)
