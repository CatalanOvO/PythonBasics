# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b  # 如果一个函数定义中包含 yield 关键字, 那么就是一个 generator 函数
#         # 调用一个generator函数将返回一个 generator
#         a, b = b, a+b
#         n = n+1
#     return 'done'
#
#
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 3
#     print('step 3')
#     yield 5
#
#
# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))
# # print(next(o)) 执行3次yield之后, 已经没有yield可以执行了, 所以第4次会报错
# print(next(odd()))
# print(next(odd()))
# print(next(odd()))
# # odd()会创建一个新的 generator 对象, 这样就创建了三个完全独立的 generator

def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]


n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')