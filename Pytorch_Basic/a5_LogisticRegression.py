import torch
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt


x_data = torch.Tensor([[1.0], [2.0], [3.0]])
y_data = torch.Tensor([[0], [0], [1]])


class LogisticRegressionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        y_pred = F.sigmoid(self.linear(x))
        return y_pred


model = LogisticRegressionModel()

criterion = torch.nn.BCELoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(1000):
    y_pred = model(x_data)
    loss = criterion(y_pred, y_data)
    print(epoch, loss.item())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


x_test = torch.Tensor([4.0])
y_test = model(x_test)
print('y_pred=', y_test.item())

x = np.linspace(0, 10, 200)
x_t = torch.Tensor(x).view((200, 1))
# 先将数组转换为Tensor, 然后通过view函数将其变为形状为(200,1)的二维张量
# PyTorch 期望输入是 (batch_size, num_features) 的二维张量
y_t = model(x_t)
y = y_t.data.numpy()
# 将张量转换为numpy的数组, 方便后续绘图
plt.plot(x, y)
plt.plot([0, 10], [0.5, 0.5], c='r')  # 添加一条x范围[0,10], y固定为0.5, 颜色为红色的线
plt.xlabel('Hours')
plt.ylabel('Probability of Pass')
plt.grid()  # 添加网格线
plt.show()
