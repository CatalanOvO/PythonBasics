import matplotlib.pyplot as plt
import numpy as np

# 生成输入序列表示
X = np.array([[0.1, 0.2, 0.3, 0.4],
             [0.5, 0.6, 0.7, 0.8],
             [0.9, 1.0, 1.1, 1.2]])

# 计算自注意力权重
W = np.array([[0.2, 0.3, 0.4, 0.5],
             [0.5, 0.6, 0.7, 0.8],
             [1.0, 1.1, 1.2, 1.3]])


Q = X.dot(W.T)  # Query
K = X.dot(W.T)  # Key
V = X.dot(W.T)  # Value

# 计算注意力分数矩阵
A = np.exp(Q.dot(K.T)) / np.sqrt(Q.shape[-1])
# 除以维度的平方根是为了缩放点积, 防止在计算注意力分数时结果过大
A /= A.sum(axis=-1, keepdims=True)
# axis=-1沿着最后一维运算(二维时是按行), keepdims: 结果保持维度(这里如果是False得出的是1*n, True则n*1

# 计算自注意力输出
Z = A.dot(V)

# 绘制图像
plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.imshow(A, cmap='hot', interpolation='nearest')
plt.title('Attention Weights')
plt.colorbar()

plt.subplot(122)
plt.imshow(Z, cmap='hot', interpolation='nearest')
plt.title('Attention Output')
plt.colorbar()

plt.tight_layout()
plt.show()
