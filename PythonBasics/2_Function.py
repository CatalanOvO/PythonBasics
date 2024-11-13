# a = abs
# print(a(-2))

# n1=1000
# print(str(hex(n1)))
#
# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if(x>=0):
#         return x
#     else:
#         return -x;
#
# from PythonBasics import my_abs
#
# def nop():
#     pass # 占位符, 以后再来补充

# import math
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# x, y = move(100, 100, 60, math.pi/6)
# print(x, y)
# r = move(100, 100, 60, math.pi/6)
# print(r) # 函数的返回值是 tuple !

# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
# def enroll(name, gender, age=6, city='Chengdu'):
#     print('name:',name)
#     print('gender:',gender)
#     print('age:',age)
#     print('city:',city)
# enroll('Adam','M',city='Beijing')
#
# def add_end(L=[]):
#     L.append('End')
#     return L
# print(add_end())
# print(add_end())
# print(add_end())
# Python函数在定义的时候, 默认参数 L 的值就被计算出来了, 即 []
# 因为默认参数 L 也是一个变量, 它指向对象[]
# 每次调用该函数, 如果改变了 L 的内容, 则下次调用时, 默认参数的内容就变了！

# 因此, 定义默认参数时牢记——默认参数必须指向不变参数
# 修改:
# def add_end_2(L=None):
#     if L is None:
#         L=[]
#     L.append('END')
#     return L
#
# # 可变参数
# def calc(*numbers): # 在函数内部, 参数numbers接收到的是一个tuple
#     sum = 0
#     for n in numbers:
#         sum = sum + n*n
#     return sum
# # 两种调用方式:
# print(calc(1,2,3))
# nums = [1,2,3,4]
# print(calc(*nums)) # Python允许在list或者tuple前面加一个*号, 把list或tuple的元素变成可变参数传进去

# 关键字参数 kwargs(Keyword Arguments)
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
# print(person('Mike', 30, city={'Beijing'}, game={'Genshin'}))
# 由于person没有返回值, 所以第二行还会输出一个None
#
# extra = {'city': 'Beijing', 'job': 'Tea'}
# print(person('Jack', 24, city=extra['city'], job=extra['job']))
# print(person('Jack', 24, **extra))
# **extra表示把extra这个dict的所有 key-value 用关键字参数传入到函数的 **kw参数, kw将获得一个dict
# 注意 kw 获得的dict是extra的一份拷贝, 对kw的改动不会影响到函数外的extra

# # 命名关键字
# def person(name, age, **kw):
#     if 'city' in kw:
#         pass
#     if 'job' in kw:
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)
# print( person('Jack', 24, city='Beijing', job='Tea') )

# def person(name, age, city, job):
#     print(name, age, city, job)
# # 与关键字参数 **kw 不同, 命名关键字参数需要一个特殊分隔符*, *后面的参数被视为命名关键字参数

# def person(name, age, *args, city):
#     print(name, age, args, city)
# # 如果函数定义中已经有了一个可变参数, 后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# # 命名关键字参数必须传入参数名！这和位置参数不同

# def person(name, age, *, city='Beijing', job):
#     print(name, age, city, job)
# person('Jack', 20, job='Teacher')
# # 命名关键字参数可以有缺省值, 调用时可以不传入 city参数

# def f1(a, b, c=0, *args, **kw):
#     print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
#
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
#
#
# args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
# f1(*args, **kw)
# args = (1, 2, 3)
# kw = {'d': 88, 'x': '#'}
# f2(*args, **kw)
# # 对于任何函数, 都可以通过类似 func(*args,**kw)的形式调用它, 无论它的参数是如何定义的
# # *: 收集任意数量的位置参数, 收集为元组(tuple)
# # **: 收集任意数量的关键字参数, 收集为字典(dict)

# def mul(*nums):
#     if nums == ():
#         raise TypeError('未输入参数')
#     pai = 1
#     for x in nums:
#         pai = pai * x
#     return pai
#
#
# # 测试
# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
# if mul(5) != 5:
#     print('mul(5)测试失败!')
# elif mul(5, 6) != 30:
#     print('mul(5, 6)测试失败!')
# elif mul(5, 6, 7) != 210:
#     print('mul(5, 6, 7)测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#     print('mul(5, 6, 7, 9)测试失败!')
# else:
#     try:
#         mul()
#         print('mul()测试失败!')
#     except TypeError:
#         print('测试成功!')

# # 函数调用通过栈实现, 每当进入一个函数调用, 栈就会加一层栈帧; 每当函数返回则栈减少一层栈帧
# def fact(n):
#     return fact_iter(n, 1)
#
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num-1, num*product)
# # 尾递归: 在函数返回时, 调用自身本身并且return语句不包含表达式
# # 这样编译器/解释器就可以把尾递归做优化, 使递归本身无论调用多少次, 都只占用一个栈帧, 不会出现栈溢出
# # 尾递归优化解决调用栈溢出, 循环可以看作一种特殊的尾递归函数
# # return n*fact(n-1) 引入了乘法表达式, 不是尾递归

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    move(n-1, a, c, b)   # 上面的n-1个从A挪到B
    move(1, a, b, c)  # 最下面的那个从A挪到C
    move(n-1, b, a, c)   # B的全部挪到C


move(3, 'A', 'B', 'C')
