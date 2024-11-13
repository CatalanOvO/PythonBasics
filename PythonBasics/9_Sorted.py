# l = [36, 5, -12, 9, -21]
# print(sorted(l))
# print(sorted(l, key=abs))
# """
# 对比原始的list和经过key=abs的处理过的list:
# list = [36, 5, -12, 9, -21]
# keys = [36, 5,  12, 9,  21]
# 然后sorted函数按照keys进行排序，并按照对应关系返回list相应的元素
# """
# l = ['bob', 'about', 'Zoo', 'Credit']
# print(sorted(l))
# # 注意: 'Z'<'a'

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score)
print(L2)
