#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Python3 列表
    Python包含6中内建的序列，即列表、元组、字符串、Unicode字符串、buffer对象和xrange对象。
    通用序列操作：索引、分片、序列相加、乘法、成员资格、长度、最小值和最大值
    序列都可以进行的操作包括索引，切片，加，乘，检查成员
    更新列表
        你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项，
    删除列表元素
        可以使用 del 语句来删除列表的的元素
    Python列表脚本操作符
        列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
    嵌套列表
        使用嵌套列表即在列表里创建其它列表
    Python列表函数&方法
        序号	函数
        1	len(list)        列表元素个数
        2	max(list)        返回列表元素最大值
        3	min(list)        返回列表元素最小值
        4	list(seq)        将元组转换为列表
        序号	方法
        2	list.count(obj)        统计某个元素在列表中出现的次数
        4	list.index(obj)        从列表中找出某个值第一个匹配项的索引位置

        1	list.append(obj)       在列表末尾添加新的对象
        3	list.extend(seq)       在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
        5	list.insert(index, obj)将对象插入列表

        6	list.pop(obj=list[-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
        7	list.remove(obj)       移除列表中某个值的第一个匹配项
        10	list.clear()           清空列表

        8	list.reverse()         反向列表中元素
        9	list.sort([func])      对原列表进行排序
        11	list.copy()            复制列表
'''

import sys

def loop_list():
    '''list加序号的遍历方式'''
    title = ["姓名", "性别", "年龄", "生日", "电话", "住址"]
    for title_id, title_text in enumerate(title):
        print(title_id, title_text)
    for title_id, title_text in zip(range(0, len(title)), title):
        print(title_id, title_text)

def main(argv):
    '''主函数'''
    print("运行参数", argv)
    print(__doc__)
    loop_list()

if __name__ == "__main__":
    main(sys.argv)
