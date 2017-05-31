#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Python3 面向对象
    面向对象技术简介
        类(Class): 用来描述具有相同的属性和方法的对象的集合。
            它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
        类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。
            类变量通常不作为实例变量使用。
        数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
        方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，
            这个过程叫方法的覆盖（override），也称为方法的重写。
        实例变量：定义在方法中的变量，只作用于当前实例的类。
        继承：即一个派生类（derived class）继承基类（base class）的字段和方法。
            继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：
            一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
        实例化：创建一个类的实例，类的具体对象。
        方法：类中定义的函数。
        对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
            和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。
            Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，
                派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
            对象可以包含任意数量和类型的数据。
        类定义
            语法格式
        类对象
            类对象支持两种操作：属性引用和实例化。
            属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
            类对象创建后，类命名空间中所有的命名都是有效属性名。
            很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法（构造方法）
            类定义了 __init__() 方法的话，类的实例化操作会自动调用 __init__() 方法。
            当然， __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上。
        self代表类的实例，而非类
            类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
        类的方法
            在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数:
        继承
            Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示
            需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，
                python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法。
        多继承
            Python同样有限的支持多继承形式。
            需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，
                python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
        方法重写
            如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，
        类属性与方法
            类的私有属性
                __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。
                    在类内部的方法中使用时 self.__private_attrs。
            类的方法
                在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，
                    类方法必须包含参数self,且为第一个参数
            类的私有方法
                __private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。
                    在类的内部调用 self.__private_methods。
        类的专有方法：
            __init__ : 构造函数，在生成对象时调用
            __del__ : 析构函数，释放对象时使用
            __repr__ : 打印，转换
            __setitem__ : 按照索引赋值
            __getitem__: 按照索引获取值
            __len__: 获得长度
            __cmp__: 比较运算
            __call__: 函数调用
            __add__: 加运算
            __sub__: 减运算
            __mul__: 乘运算
            __div__: 除运算
            __mod__: 求余运算
            __pow__: 称方
        运算符重载
            Python同样支持运算符重载，我么可以对类的专有方法进行重载，实例如下：

        实例分析:GirlStudent(Women, Student)  --> (People)  如果Women中使用super(),结果调用了Student的say
            方法,原因可能是多层继承的原因造成的.

'''

import sys

class People:
    '''人'''
    attrs = {}
    attrs['name'] = ''
    attrs['age'] = 0
    attrs['address'] = ''
    attrs['height'] = 0
    attrs['weight'] = 0

    #name, age, height, weight, address
    def __init__(self, **kw):
        '''构造函数'''
        for arg_name, arg_value in kw.items():
            if arg_name in self.attrs.keys():
                self.attrs[arg_name] = arg_value
        print(People, self, "构造函数")

    def say(self):
        '''输出函数'''
        print('People说:我是一个人。我的姓名是{}，年龄是{}，身高{}CM，体重{}KG，地址是{}。'.format(
            self.attrs['name'], self.attrs['age'], self.attrs['height'],
            self.attrs['weight'], self.attrs['address']))

    def print_type(self):
        '''打印类对象'''
        print(People.__class__, self)

class Student(People):
    '''学生'''
    #name, age, height, weight, address, score
    def __init__(self, **kw):
        '''构造函数'''
        super().__init__(**kw)
        self.attrs['score'] = kw['score']
        print(Student, self, "构造函数")

    def say(self):
        '''输出函数'''
        super().say()
        print('Student说:我的分数是{}'.format(self.attrs['score']))

class Women(People):
    '''女人'''
    #name, age, height, weight, address
    def __init__(self, **kw):
        '''构造函数'''
        People.__init__(self, **kw)
        self.attrs['sex'] = '女'
        print(Women, self, "构造函数", super())


    def say(self):
        '''输出函数'''
        super().say()
        print('Women说:我的性别是{}'.format(self.attrs['sex']))

class GirlStudent(Women, Student):
    '''女学生'''
    #name, age, height, weight, address, score
    def __init__(self, **kw):
        '''构造函数'''
        Women.__init__(self, **kw)
        Student.__init__(self, **kw)
        print(GirlStudent, self, "构造函数")


def main(argv):
    '''主函数'''
    print("运行参数", argv)
    print(__doc__)
    jerry = GirlStudent(name='Jerry', age=12, height=158, weight=45, address='美国', score=120)
    jerry.say()

if __name__ == "__main__":
    main(sys.argv)
