import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

np.random.seed(42)
n_sample = 1000
X = np.random.uniform(500, 5000, size=n_sample)  # 房屋面积
y = 0.05 * X ** 2 - 20 * X + 3000 + np.random.normal(0, 20000, size=n_sample)  # 房屋价格+噪声

X = X.reshape(-1, 1)  # 列数为1, 行数不确定

degrees = [1, 2, 3, 4]

plt.figure(figsize=(12, 8))

residuals = []

for i, degree in enumerate(degrees, 1):  # 1是start
    ploy_features = PolynomialFeatures(degree=degree)
    X_ploy = ploy_features.fit_transform(X)

    model = LinearRegression()
    model.fit(X_ploy, y)
    y_pred = model.predict(X_ploy)
    residuals.append(y - y_pred)

    # 1. Actual Data vs Polynomial Fit
    plt.subplot(2, 2, 1)
    X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    X_range_poly = ploy_features.transform(X_range)
    y_range_pred = model.predict(X_range_poly)
    plt.scatter(X, y, color='gray', alpha=0.6, label='Actual Data' if i == 1 else '', s=10)
    # 仅在i=1时添加真实数据的曲线, s=10设置散点大小
    plt.plot(X_range, y_range_pred, label=f'Degree {degree} fit', linewidth=2)
    plt.xlabel('House size (sq ft)')
    plt.ylabel('Price ($1000)')
    plt.title('Actual Data vs Polynomial Fit')
    plt.legend()

    # 2. Residual
    plt.subplot(2, 2, 2)
    plt.scatter(X, residuals[i - 1], alpha=0.7, label=f'Degree {degree} Residuals', s=10)
    plt.hlines(0 , X.min(), X.max(), colors='black', linestyles='dashed')
    plt.xlabel('House size (sq ft)')
    plt.ylabel('Residuals')
    plt.title('Residuals Analysis')
    plt.legend()

    # 3. MSE vs Polynomial Degree
    plt.subplot(2, 2, 3)
    mse = mean_squared_error(y, y_pred)
    plt.scatter(degree, mse, color='red', s=50, zorder=5)
    # 设置该点的绘制顺序, 数值越大, 点越靠上绘制, 这样可以确保它在其他图形元素之上, 增加可见性
    plt.plot(degrees[:i], [mean_squared_error(y, model.fit
                                (PolynomialFeatures(deg).fit_transform(X), y)
                                .predict(PolynomialFeatures(deg).fit_transform(X)))
                           for deg in degrees[:i]], color='blue', linewidth=2, label='MSE vs Degree')
    plt.xlabel('Polynomial Degree')
    plt.ylabel('Mean Squared Error')
    plt.title('MSE vs Polynomial Degree')
    plt.grid(True)
    if i == 1:
        plt.legend()


plt.tight_layout()
plt.show()
