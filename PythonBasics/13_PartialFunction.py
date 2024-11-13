import functools
"""
Python的functools模块提供了很多有用的功能, 其中之一就是偏函数(Partial Function)
注意这里的偏函数和数学意义上的偏函数不一样
"""
print(int('12345'))  # 12345
print(int('12345', base=8))  # 5349
print(int('12345', 16))  # 74565


def int2(x, base=2):
    return int(x, base)


# functools.partial的作用就是把一个函数的某些参数给固定住(即设置默认值), 返回一个新的函数, 调用这个新函数会更简单
int2 = functools.partial(int, base=2)
# int2('10010') 相当于 kw = {'base': 2} int('10010', **kw)

max2 = functools.partial(max, 10)  # 实际上会把10作为*args的一部分自动加到左边
# max2(5, 6, 7) 相当于 args = (10, 5, 6, 7)  max(*args)

