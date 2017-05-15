'''
模板文件
'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

def info():
    '''
    这是模板文件
    '''
    print(info.__doc__)

def main(argv):
    '''
    主函数
    '''
    print("运行参数", argv)
    info()


if __name__ == "__main__":
    main(sys.argv)
