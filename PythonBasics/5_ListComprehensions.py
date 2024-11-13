# print([i*i for i in range(1, 11) if i % 2 == 0])
# print([m + n for m in 'ABC' for n in 'XYZ'])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [item.lower() for item in L1 if isinstance(item, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')