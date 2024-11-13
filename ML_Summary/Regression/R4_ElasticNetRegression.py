import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)
X = np.random.rand(1000, 10)
coefficients = np.array([1.5, -2.0, 3.0, 0, 0, 0, 0.5, -1.5, 2.0, -3.0])
y = X @ coefficients + np.random.randn(1000) * 0.5

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.7, random_state=42)
# 设定 alpha l1_ratio 构建一个弹性网络回归模型, 既进行特征选择又减轻多重共线性问题
elastic_net.fit(X_train_scaled, y_train)

y_pred = elastic_net.predict(X_test_scaled)
coefficients = elastic_net.coef_

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Elastic Net Regression Analysis', fontsize=16)

# 1. Residuals Plot
residuals = y_test - y_pred
axs[0, 0].scatter(y_pred, residuals, color='red', edgecolor='k')
axs[0, 0].axhline(0, color='black', linestyle='--')
axs[0, 0].set_title('Residuals vs Fitted')
axs[0, 0].set_xlabel('Fitted values')
axs[0, 0].set_ylabel('Residuals')

# 2. Coefficient Plot
axs[0, 1].bar(range(len(coefficients)), coefficients, color='blue')
axs[0, 1].set_title('Coefficient Magnitude')
axs[0, 1].set_xlabel('Feature index')
axs[0, 1].set_ylabel('Coefficient value')

# 3. Predict vs Actual Plot
axs[1, 0].scatter(y_test, y_pred, color='green', edgecolor='k')
axs[1, 0].plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='black', linestyle='--')
axs[1, 0].set_title('Predict vs Actual')
axs[1, 0].set_xlabel('Actual values')
axs[1, 0].set_ylabel('Predict values')

# 4. Residual Histogram
axs[1, 1].hist(residuals, bins=20, color='purple', edgecolor='k')
axs[1, 1].set_title('Histogram of Residuals')
axs[1, 1].set_xlabel('Residuals')
axs[1, 1].set_ylabel('Frequency')

plt.tight_layout(rect=[0.0, 0.0, 1.0, 0.96])
plt.show()
