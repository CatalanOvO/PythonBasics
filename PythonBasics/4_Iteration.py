# d = {'a': 1, 'b': 2, 'c': 3}
# for k, v in d.items():
#     pass
# for value in d.values():
#     pass
# for key in d:
#     pass

def findMinAndMax(L):
    if not L:
        return None, None
    minn, maxx = L[0], L[0]
    for i in L:
        if i > maxx:
            maxx = i
        if i < minn:
            minn = i
    return minn, maxx


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
