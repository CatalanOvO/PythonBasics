import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_data = [1.0, 2.0, 3.0]  # y=5x+8
y_data = [12.0, 18.0, 24.0]


def forward(x, w, b):
    return w * x + b


def loss(x, y, w, b):
    y_pred = forward(x, w, b)
    return (y_pred - y) * (y_pred - y)


W = np.arange(4.0, 10.1, 0.2)
B = np.arange(4.0, 10.1, 0.2)
[w, b] = np.meshgrid(W, B)

mse = np.zeros_like(w)  # 创建一个与 w 大小相同的矩阵，用于存储每个 w 和 b 组合的 MSE 值。

for x_val, y_val in zip(x_data, y_data):
    y_pred_val = forward(x_val, w, b)
    print('y_pred_val=', y_pred_val)
    mse += loss(x_val, y_val, w, b)

mse /= len(x_data)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(w, b, mse, cmap='viridis')  # cmap='viridis' 设置了颜色映射

ax.set_xlabel('w')
ax.set_ylabel('b')
ax.set_zlabel('MSE')
plt.show()
