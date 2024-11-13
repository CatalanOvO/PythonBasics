import torch

x_data = torch.Tensor([[1.0], [2.0], [3.0]])
y_data = torch.Tensor([[2.0], [4.0], [6.0]])


class LinearModel(torch.nn.Module):
    def __init__(self):
        super().__init__()  # 调用父类构造函数, 完成一些必要的初始化
        self.linear = torch.nn.Linear(1, 1)  # 创建一个线性层, 输入输出都是一维张量

    def forward(self, x):
        y_pred = self.linear(x)  # 通过线性层计算y_pred
        return y_pred


model = LinearModel()

criterion = torch.nn.MSELoss(reduction='sum')  # 损失是所有样本的损失之和
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # 模型的所有参数（权重和偏置）传给优化器

for epoch in range(100):
    y_pred = model(x_data)
    loss = criterion(y_pred, y_data)
    print(epoch, loss.item())

    optimizer.zero_grad()
    loss.backward()  # 清除之前的梯度, 防止梯度累加
    optimizer.step()  # 根据反向传播计算的梯度更新参数

print('w=', model.linear.weight.item())
print('b=', model.linear.bias.item())

x_test = torch.Tensor([[4.0]])
y_test = model(x_test)
print('y_pred =', y_test.data)
