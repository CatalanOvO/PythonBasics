import matplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = 1.0


def forward(x, w):
    return w * x


def cost(xs, ys, w):
    costs = 0
    for x, y in zip(xs, ys):
        y_pred = forward(x, w)
        costs += (y_pred - y) * (y_pred - y)
    return costs / len(xs)


def gradient(xs, ys, w):
    grad = 0
    for x, y in zip(xs, ys):
        grad += 2 * x * (forward(x, w) - y)
    return grad / len(xs)


Cost = []
Epoch = []
print('Predict (before training)', 4, forward(4, w))
for epoch in range(100):
    cost_val = cost(x_data, y_data, w)
    grad_val = gradient(x_data, y_data, w)
    step = 0.01
    w -= step * grad_val  # 一个Epoch共用一个w, 因此每一轮x_i之间互不影响
    print('Epoch:', epoch, 'w=', w, 'loss=', cost_val)
    Epoch.append(epoch)
    Cost.append(cost_val)
print('Predict (after training)', 4, forward(4, w))

plt.plot(Epoch, Cost)
plt.xlabel('Epoch')
plt.ylabel('Cost')
plt.show()
