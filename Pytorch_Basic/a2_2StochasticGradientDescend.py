import matplotlib.pyplot as plt
import random

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]


def forward(x, w):
    return x * w


def loss(x, y, w):
    y_pred = forward(x, w)
    return (y_pred - y) ** 2


def gradient(x, y, w):
    y_pred = forward(x, w)
    return 2 * x * (y_pred - y)


w = random.uniform(0.0, 8.0)
step = 0.01
print('Predict (before training:', 4, forward(4, w))
Epoch = []
Avg_Loss = []

for epoch in range(100):
    sum_loss = 0
    for x, y in zip(x_data, y_data):
        grad = gradient(x, y, w)
        w -= step * grad
        print('\tgrad: ', x, y, grad)
        sum_loss += loss(x, y, w)

    Epoch.append(epoch)
    Avg_Loss.append(sum_loss/len(x_data))
    print('progress: ', epoch, 'w=', w, 'avg_loss=', sum_loss/len(x_data))

print('Predict (after training):', 4, forward(4, w))

plt.plot(Epoch, Avg_Loss)
plt.xlabel('Epoch')
plt.ylabel('Avg_Loss')
plt.show()
