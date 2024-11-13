import numpy as np
import matplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]


def forward(x):
    return w * x


def loss(x, y):
    y_pred = forward(x)
    return (y - y_pred) ** 2
"""
这个写法使用了 Python 中的幂运算符 **。
虽然这里的指数是 2，看似简单，但一般的幂运算（即使是平方）会调用 Python 的通用幂函数（如 pow()）
因此效率略低，因为它涉及到更多的底层计算和处理。
"""


w_list = []
mse_list = []
for w in np.arange(0.0, 4.1, 0.1):  # 这里定义的w是一个全局变量, for循环结束后w还在, 值为4.0
    print('w=', w)
    l_sum = 0
    for x_val, y_val in zip(x_data, y_data):
        y_pred_val = forward(x_val)
        loss_val = loss(x_val, y_val)
        l_sum += loss_val
        print('\t', x_val, y_val, y_pred_val, loss_val)
    print('MSE=', l_sum/3)
    w_list.append(w)
    mse_list.append(l_sum/3)

plt.plot(w_list, mse_list)
plt.ylabel('loss')
plt.xlabel('w')
plt.show()
