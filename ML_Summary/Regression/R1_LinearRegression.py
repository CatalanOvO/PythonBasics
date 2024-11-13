import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 生成虚拟数据集
np.random.seed(42)
X = np.random.rand(1000, 1) * 10  # 生成1000个 0~10 之间的随机数
y = 2.5 * X + np.random.randn(1000, 1) * 3  # 生成服从线性关系的 y 值, 加上一定的噪声

# 创建线性回归模型并训练
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# 计算残差
residuals = y - y_pred

# 绘图
plt.figure(figsize=(12, 10))

# 子图1: 散点图与回归线
plt.subplot(2, 2, 1)
plt.scatter(X, y, color='blue', label='Actual Data', alpha=0.6)
plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line')
plt.title('Scatter Plot with Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()

# 子图2: 残差图
plt.subplot(2, 2, 2)
plt.scatter(X, residuals, color='green', alpha=0.6)
plt.hlines(y=0, xmin=min(X), xmax=max(X), color='red', linestyle='--')
plt.title('Residual Plot')
plt.xlabel('X')
plt.ylabel('Residuals')

# 子图3: 预测值与实际值的对比
plt.subplot(2, 2, 3)
plt.scatter(y, y_pred, color='purple', alpha=0.6)
plt.plot([min(y), max(y)], [min(y), max(y)], color='red', linestyle='--', label='Perfect Fit')
plt.title('Redict vs Actual')
plt.xlabel('Actual y')
plt.ylabel('Predict y')
plt.legend()

# 子图4: 残差直方图
plt.subplot(2, 2, 4)
plt.hist(residuals, bins=20, color='orange', edgecolor='black', alpha=0.7)
plt.title('Residuals Distribution')
plt.xlabel('Residuals')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
