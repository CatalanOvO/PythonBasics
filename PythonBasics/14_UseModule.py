#!/usr/bon/env python3
# -*- coding: utf-8 -*-

""" a test module """

__author__ = 'Catalan'

import sys


def test():
    args = sys.argv  # argv至少有一个元素, 第一个元素永远是该.py文件的名称'14_UseModule.py'
    if len(args) == 1:
        print('Hello World!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':  # 防止模块被导入时自动执行某些代码, 同时划分模块的定义和执行逻辑
    test()
"""
每个Python模块都有一个内置属性__name__，用于表示模块的名称(模块的命名空间)
如果模块是被直接运行的（例如，通过命令行或IDE），__name__ 的值将是 '__main__'。
如果模块是被导入到其他模块中使用，__name__ 的值将是该模块的名称（即文件名，不包含扩展名）。
即
math_utils.py:
    直接运行时：__name__ = '__main__'
    被导入时：__name__ = 'math_utils'
main.py:
    直接运行时：__name__ = '__main__'
    被导入时：__name__ = 'main'
"""

"""
作用域:
__xxx__ : 特殊变量, 可以被直接引用, 但是有特殊用途, 如: __author__, __name__, __doc__(文档注释), 自己的变量不要这样用
_xxx, __xxx : 非公开的(private), 不应该被直接引用(不是不能, 编程习惯, Python不能完全限制访问private函数或变量)
"""
# private函数、变量不应该被别人引用, 那它们有什么用呢？


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


"""
我们在模块里公开greeting()函数, 而把内部逻辑用private函数隐藏起来了
这样调用greeting()函数不用关心内部的private函数细节, 这也是一种非常有用的代码封装和抽象的方法, 即:
外部不需要引用的函数全部定义为private, 只有外部需要引用的函数才定义为public
"""