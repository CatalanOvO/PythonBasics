# L = [i for i in range(1, 100, 2)]
#
# print(L[:3])  # 即取 [0,3) 的所有元素
# print(L[-2:])  # 倒数第一个元素的索引是-1
#
# print(L[10:20:2])
# # print(L[:])  # 表示整个L
# print('ABCDEFG'[:3])
# print('ABCDEFG'[::2])

def trim(s):
    while s and s[0] == ' ':
        s = s[1:]
    while s and s[-1] == ' ':
        s = s[:-1]
    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')