# def _get_odd():
#     n = 1
#     while True:
#         n += 2
#         yield n
#
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
#
# def prime():
#     yield 2
#     it = _get_odd()  # it最初是全体奇数的迭代器, 后续会逐步埃氏筛过滤掉一部分合数
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
#         # it 是惰性计算的序列, 只会在需要时更新下一个
#
#
# for n in prime():
#     if n < 100:
#         print(n)
#     else:
#         break
def is_palindrome(n):
    return n == int(str(n)[::-1])


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')