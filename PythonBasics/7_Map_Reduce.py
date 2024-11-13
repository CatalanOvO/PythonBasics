# # abs = 10
# # abs(-10)
# # abs原本指向一个计算绝对值的函数, 这样操作之后abs这个变量就会指向整数10
# # 要恢复abs函数只能重启 Python 交互环境
#
# # def add(x, y, f):
# #     return f(x)+f(y)
# #
# #
# # print(add(6, -5, abs))
# def f(x):
#     return x*x
#
#
# r = map(f, [1, 2, 3, 4, 5])
# print(list(r))
# # map()传入的第一个参数是f, 即函数对象本身
# # 由于结果r是一个Iterator, 它是惰性序列, 所以需要提高list()函数让它把整个序列都计算出来并返回一个list
# # 惰性序列——你不主动遍历它, 它就不会计算其中元素的值. Python中的惰性序列大多指iterator
# list(map(str, [1, 2, 3, 4, 5]))
#
# # reduce(f, [x, y, z, w]) = f(f(f(x, y), z), w)s
# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#
# def str2int(s):
#     def fn(x, y):
#         return x*10 +y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))
#
#
# print(str2int('13579'))

# from functools import reduce
#
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#
# def char2num(s):
#     return DIGITS[s]
#
#
# def str2int(s):
#     return reduce(lambda x, y: x*10 + y, map(char2num, s))

# def normalize(name):
#     return name[0].upper() + name[1:].lower()
#
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
# from functools import reduce
#
# def prod(L):
#     return reduce(lambda x, y: x*y, L)
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

from functools import reduce

def str2float(s):

    return reduce(lambda x, y: 10*x + y, map(lambda x: DIGITS[x], s))


def str2float(s):
    DIGITS = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }
    i = s.find('.')
    if i == -1:
        return reduce(lambda x, y: x*10 + y, map(lambda x: DIGITS[x], s))
    s1 = s[:i] + s[i+1:]
    return reduce(lambda x, y: x*10 + y, map(lambda  x: DIGITS[x], s1)) * 0.1 ** (len(s) -i -1)



print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
