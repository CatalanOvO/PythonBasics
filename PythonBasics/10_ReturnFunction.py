# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum  # 生成一个新的sum函数实例, 使得f1和f2是两个不同的函数实例
#     # 注: 如果是return sum(), 则是调用sum()并返回其结果
#
#
# f1 = lazy_sum(1, 3, 5, 7, 9)
# f2 = lazy_sum(1, 3, 5, 7, 9)
# print(f1 == f2)
# print(f1())
"""
在这个例子中, 我们在函数lazy_sum中又定义了函数sum, 并且内部函数sum可以引用外部函数lazy_sum的参数和局部变量
当lazy_sum返回函数sum时, 相关参数和变量都保存在返回的函数中, 这是称为“闭包(closure)”的程序结构
"""

# 注意到返回的函数在其定义内部引用了局部变量args, 所以当一个函数返回了一个函数后
# 其内部的局部变量还被新函数引用. 所以闭包用起来简单, 实现起来可不容易
# 此外, 返回的函数并没有立刻执行, 而是直到调用了 f() 才执行
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
#
#
# f1, f2, f3 = count()
# print(f1())
# # print(f2())
# # print(f3())
"这样返回的都是9 ———— 因为返回的函数引用了变量i, 但它并非立刻执行. 等到3个函数都返回时, i已经变成3了"
"返回闭包时牢记 ———— 返回函数不要引用任何循环变量or后续会改变的变量"

"如果一定要引用循环变量?方法是再创建一个函数, 用该函数的参数绑定循环变量当前的值！"


# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))  # f(i)被立刻执行, 因此i的当前值被传入f()
#     return fs
#
#
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())

"nonlocal"
"使用闭包, 就是内层函数引用了外层函数的局部变量. 如果只是读外层变量的值, 我们会发现返回的闭包函数调用一切正常"
# def inc():
#     x = 0
#     def fn():
#         # 仅读取x的值
#         return x + 1
#     return fn
#
#
# f = inc()
# print(f())  # 1
# print(f())  # 1

"但是, 如果对外层变量赋值, 由于Python解释器会把x当作函数fn()的局部变量, 它会报错"
# def inc():
#     x = 0
#     def fn():
#         nonlocal x
#         x = x + 1  # 如果不加上一句nonlocal x会报错, 因为 x 作为局部变量没有初始化, 不能直接计算
#         return x
#     return fn


def createCounter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
