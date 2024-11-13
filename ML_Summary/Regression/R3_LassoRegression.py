import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# 生成虚拟数据
np.random.seed(42)
n_samples = 1000
n_features = 10

# 生成随机特征数据矩阵
X = np.random.randn(n_samples, n_features)

# 生成权重, 其中部分权重为0, 模拟实际不相关特征
true_coef = np.array([10, -5, 0, 0, 3, 0, 2, 0, 0, 1])

# 生成目标变量, 并添加噪声
y = np.dot(X, true_coef) + np.random.normal(0, 1, size=n_samples)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 数据标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

# Lasso回归模型
lasso = Lasso(alpha=0.1)  # L1正则化强度
lasso.fit(X_train_scaled, y_train)

# 预测
y_pred_train = lasso.predict(X_train_scaled)
y_pred_test = lasso.predict(X_test_scaled)

mse_test = mean_squared_error(y_test, y_pred_test)

# 绘图
plt.figure(figsize=(12, 8))

# 1. 特征重要性条形图
plt.subplot(2, 2, 1)
plt.bar(np.arange(n_features), lasso.coef_, color='cyan', label='Lasso Coefficients')
plt.axhline(0, color='black', linestyle='--')
plt.xlabel('Feature Index')
plt.ylabel('Coefficient Value')
plt.title('Feature Importance (Lasso Coefficients)')
plt.legend()

# 2. 实际值 vs 预测值的散点图
plt.subplot(2, 2, 2)
plt.scatter(y_test, y_pred_test, color='magenta', edgecolor='black', label='Predict vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='blue',
         lw=2, linestyle='--', label='Ideal Fit')
plt.xlabel('Actual Value')
plt.ylabel('Predict Value')
plt.title(f'Predict vs Actual (MSE={mse_test:.2f}')
plt.legend()

# 3. 残差图
plt.subplot(2, 2, 3)
residuals = y_test - y_pred_test
plt.scatter(y_pred_test, residuals, color='orange', edgecolor='black', label='Residuals')
plt.axhline(0, color='black', linestyle='--')
plt.xlabel('Predict Value')
plt.ylabel('Residuals')
plt.title('Residuals Plot')
plt.legend()

# 4. 特征与目标值的散点图 + 回归线(针对前两个特征)
plt.subplot(2, 2, 4)
for i in range(2):
    plt.scatter(X_test_scaled[:, i], y_test, color=np.random.rand(3,), edgecolor='black', label=f'feature {i+1}')
    plt.plot(X_test_scaled[:, i], lasso.predict(X_test_scaled), color=np.random.rand(3,), lw=2, linestyle='--')

plt.xlabel('Feature Value')
plt.ylabel('Target Value')
plt.title('Feature vs Target with Lasso Fit')
plt.legend()

plt.tight_layout()
plt.show()
