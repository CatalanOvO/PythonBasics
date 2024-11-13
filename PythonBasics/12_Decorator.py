def now():
    print('2024-6-1')


f = now
print(f())
print(now.__name__)  # now
print(f.__name__)  # now
"""
现在, 假设我们要增强now()函数的功能, 比如在函数调用后自动打印日志, 但又不希望修改now()函数的定义
这种在代码运行期间动态增加功能的方式, 称为"装饰器"(Decorator)
本质上, decorator就是一个返回函数的高阶函数.
"""
# 定义一个能打印日志的decorator:
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


