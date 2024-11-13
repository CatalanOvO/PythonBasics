# student = ['A', 'B', 'C']
# # 可以用 -1 做索引获取最后一个元素
# student[-1]
# # 依次类推，获取倒数第二个、倒数第三个
# student[-2]
# print(student[-3])
# # student[-4] # 越界！
# student.append('Catty')
# student.pop(1)
# print(student)
#
#
# t = (2,1) # tuple，指向不可变
# t = (1)  #表示数
# t = (1,) #表述tuple
#
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Bob']
# ]
# print(L[0][0])
# print(L[1][1])

# L = ['Bart', 'Lisa', 'Tom']
# for name in L:
#     print(f'Hello, {name}!')

# names = {'Bart':90, 'Lisa':91, 'Tom':99}
# names.pop('Tom')

# nums = {1,1,2,2,3,4,5,5}
# print(nums)
# nums.add(5)
# nums.remove(3)
# nums2 = {1,2,3}
# print(nums&nums2)
# print(nums|nums2)

# 不可变对象
a = 'abc'
print(a.replace('a','A'))
print(a)
# 这里a是变量, 'abc'才是字符串对象
# a 本身是一个变量, 它指向的对象的内容才是'abc'
