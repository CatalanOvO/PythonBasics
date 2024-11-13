import torch

x_data = [1.0, 2.0, 3.0]  # x^2 + 2x + 3
y_data = [6.0, 11.0, 18.0]

# w1 = torch.Tensor([1.0])
# w2 = torch.Tensor([1.0])
# b = torch.Tensor([1.0])
# w1.requires_grad, w2.requires_grad, b.requires_grad = True, True, True
'随机初始化权重和偏置'
w1 = torch.randn(1, requires_grad=True)
w2 = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)


def forward(x):
    return w1 * x * x + w2 * x + b


def loss(x, y):
    y_pred = forward(x)
    return ((y_pred - y) ** 2).mean()
    # 损失函数可以使用均方误差的平均值，而不是直接平方和，这样在多个样本时会更加稳定。


print('Predict (before training):', 4, forward(torch.Tensor([4])).item())
step = 0.01
for epoch in range(100):
    for x, y in zip(x_data, y_data):
        l = loss(x, y)
        l.backward()

        print('\tgrads:', x, y, 'w1:', w1.grad.item(), '| w2:', w2.grad.item(),\
              '| b:', b.grad.item())
        w1.data -= step * w1.grad.data
        w2.data -= step * w2.grad.data
        b.data -= step * b.grad.data

        w1.grad.data.zero_()
        w2.grad.data.zero_()
        b.grad.data.zero_()
    print('Progress:', epoch, l.item())

print('Predict (after training):', 4, forward(torch.Tensor([4])).item())
