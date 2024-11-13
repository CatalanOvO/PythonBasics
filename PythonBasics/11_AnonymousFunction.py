# l = list(map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(l)
# # 关键字lambda表示匿名函数, 冒号前面的x表示函数参数
# # 匿名函数的限制: 只能有一个表达式, 不用写return, 返回值就是该表达式的结果
# # 匿名函数有个好处: 函数没有名字但是是一个函数对象, 所以不必担心函数名冲突, 可以把匿名函数赋值给一个变量, 再用该变量来调用该函数
# f = lambda x: x*x
# print(f(5))
#
#
# def build(x, y):
#     return lambda: x*x + y*y
L = list(filter(lambda x: x & 1 > 0, range(1, 20)))

print(L)
