import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# 生成虚拟数据集
np.random.seed(42)
X = np.random.rand(1000, 5)  # 1000个样本, 5个特征
y = 3 * X[:, 0] + 1.5 * X[:, 1] - 2 * X[:, 2] + np.random.randn(1000)  # 线性组合加噪声

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 标准化特征
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

# 设置不同的 a 值来训练岭回归模型
alphas = np.logspace(-4, 4, 100)
ridgecv = RidgeCV(alphas=alphas, store_cv_values=True)
ridgecv.fit(X_train_scaled, y_train)

# 预测
y_train_pred = ridgecv.predict(X_train_scaled)
y_test_pred = ridgecv.predict(X_test_scaled)

# 计算均方误差
mse_train = mean_squared_error(y_train, y_train_pred)
mse_test = mean_squared_error(y_test, y_test_pred)

# 岭回归系数路径
ridge_coefs = []
for alpha in alphas:
    ridge = Ridge(alpha = alpha)
    ridge.fit(X_train_scaled, y_train)
    ridge_coefs.append(ridge.coef_)

# 创建图像
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# 图1: 散点图和回归曲线
axs[0, 0].scatter(X_test[:, 0], y_test, color='blue', label='True Values', s=40, alpha=0.6)
axs[0, 0].scatter(X_test[:, 0], y_test_pred, color='red', label='Predicted Values', s=40, alpha=0.6)
axs[0, 0].set_title('Scatter Plot with Regression Curve', fontsize=14)
axs[0, 0].set_xlabel('Feature 1', fontsize=12)
axs[0, 0].set_ylabel('Target', fontsize=12)
axs[0, 0].legend()

# 图2: 残差图
axs[0, 1].scatter(y_test_pred, y_test_pred - y_test, color='green', s=40, alpha=0.6)
axs[0, 1].hlines(y=0, xmin=min(y_test_pred), xmax=max(y_test_pred), colors='red', linestyle='dashed')
axs[0, 1].set_title('Residual Plot', fontsize=14)
axs[0, 1].set_xlabel('Predicted Values', fontsize=12)
axs[0, 1].set_ylabel('Residuals', fontsize=12)

# 图3: 岭回归系数路径
axs[1, 0].plot(alphas, ridge_coefs)
axs[1, 0].set_xscale('log')
axs[1, 0].set_title('Ridge Coefficients as a Function of the Regularization', fontsize=14)
axs[1, 0].set_xlabel('Alpha', fontsize=12)
axs[1, 0].set_ylabel('Coefficients', fontsize=12)

# 图4: MSE曲线
cv_values_mean = np.mean(ridgecv.cv_values_, axis=0)
axs[1, 1].plot(alphas, cv_values_mean, color='purple', label='Mean CV Error')
axs[1, 1].set_xscale('log')
axs[1, 1].set_title('Mean Cross-Validation Error', fontsize=14)
axs[1, 1].set_xlabel('Alpha', fontsize=12)
axs[1, 1].set_ylabel('Mean Squared Error', fontsize=12)
axs[1, 1].legend()

plt.tight_layout()
plt.show()

"""
1. 散点图和回归曲线:
    帮助我们查看自变量与目标变量之间的实际关系以及模型拟合的效果, 比较真实值和预测值的差异, 判断模型是否合理
2. 残差图:
    用于分析预测值与实际值的差异是否具有系统性的偏差, 检查模型假设是否被满足, 是否存在任何未捕捉的趋势
3. 岭回归系数路径:
    展示了不同正则化强度下模型系数的变化, 帮助我们直观了解正则化对模型复杂度的影响
4. MSE曲线:
    展示不同alpha值下模型在交叉验证中的表现, 用来选出最优的正则化参数, 帮助我们减少过拟合
这些图结合起来, 可以多维度地分析岭回归模型的效果, 评估模型的预测能力和正则化对结果的影响.
"""
