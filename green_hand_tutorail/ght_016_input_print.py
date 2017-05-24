#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Python3 输入和输出
    输出格式美化
        Python两种输出值的方式: 表达式语句和 print() 函数。
        第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
        如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
        如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
        str()： 函数返回一个用户易读的表达形式。
        repr()： 产生一个解释器易读的表达形式。
    str.format() 的基本使用如下:
        括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
        在括号中的数字用于指向传入对象在 format() 中的位置
        如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
        '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
        可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
        如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
            最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值
    旧式字符串格式化
        % 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串,
            而将右边的代入, 然后返回格式化后的字符串.
        因为 str.format() 比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。
            但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().
    读取键盘输入
        Python提供了 input() 置函数从标准输入读入一行文本，默认的标准输入是键盘。
        input 可以接收一个Python表达式作为输入，并将运算结果返回。
    读和写文件
        open() 将会返回一个 file 对象，基本语法格式如下:
            open(filename, mode)
            filename：filename 变量是一个包含了你要访问的文件名称的字符串值。
            mode：mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。
                这个参数是非强制的，默认文件访问模式为只读(r)。rwa b +
    文件对象的方法
        本节中剩下的例子假设已经创建了一个称为 f 的文件对象。
        f.read()
            为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
        f.readline()
            f.readline() 会从文件中读取单独的一行。换行符为 '\n'。
            f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
        f.readlines()
            f.readlines() 将返回该文件中包含的所有行。
            如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
        f.write()
            f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
        f.tell()
            f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
        f.seek()
            如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
            from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
            seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
            seek(x,1) ： 表示从当前位置往后移动x个字符
            seek(-x,2)：表示从文件的结尾往前移动x个字符
            from_what 值为默认为0，即文件开头。
        f.close()
            在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。
            当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。
    pickle 模块
        python的pickle模块实现了基本的数据序列和反序列化。
        通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
        通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
        基本接口：
            pickle.dump(obj, file, [,protocol])
            pickle.load(file)
                有了 pickle 这个对象, 就能对 file 以读取的形式打开: x = pickle.load(file)
'''

import sys
import math

def print_test():
    '''输出测试'''
    print('{1} 和 {0}'.format('Google', 'Runoob'))
    print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
    print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
    print('常量 PI 的值近似为： {!r}。'.format(math.pi))
    print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
    table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
    print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

def save_obj_to_file():
    '''保存对象到文件'''
    import pickle
    # 使用pickle模块将数据对象保存到文件
    data1 = {'a': [1, 2.0, 3, 4+6j],
             'b': ('string', u'Unicode string'),
             'c': None}

    selfref_list = [1, 2, 3]
    selfref_list.append(selfref_list)

    output = open('temp_file/data.pkl', 'wb')

    # Pickle dictionary using protocol 0.
    pickle.dump(data1, output)

    # Pickle the list using the highest protocol available.
    pickle.dump(selfref_list, output, -1)

    output.close()

def laod_obj_from_file():
    '''读去对象从文件中'''
    import pprint
    import pickle
    #使用pickle模块从文件中重构python对象
    pkl_file = open('temp_file/data.pkl', 'rb')

    data1 = pickle.load(pkl_file)
    pprint.pprint(data1)

    data2 = pickle.load(pkl_file)
    pprint.pprint(data2)

    pkl_file.close()

def main(argv):
    '''主函数'''
    print("运行参数", argv)
    print(__doc__)
    print_test()
    save_obj_to_file()
    laod_obj_from_file()

if __name__ == "__main__":
    main(sys.argv)
