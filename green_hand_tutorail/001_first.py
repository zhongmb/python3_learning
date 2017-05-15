#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

def info():
    '''
    我们可以使用以下命令来查看我们使用的Python版本：
    python -V
    '''
    print(info.__doc__)

def main(argv):
    info()
    print("你好,小明")


if __name__ == "__main__":
    main(sys.argv)