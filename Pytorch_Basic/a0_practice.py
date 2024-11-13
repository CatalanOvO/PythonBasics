import torch
import matplotlib.pyplot as plt


x_data = torch.Tensor([[1.0], [2.0], [3.0]])
y_data = torch.Tensor([[2.0], [4.0], [6.0]])


class LinearModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred


model = LinearModel()

criterion = torch.nn.MSELoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

Loss = []
for epoch in range(100):
    y_pred = model(x_data)
    loss = criterion(y_pred, y_data)
    print(epoch, loss.item())

    optimizer.zero_grad()
    loss.backward()
    Loss.append(loss.item())
    optimizer.step()

print('w=', model.linear.weight.item(), '\nb=', model.linear.bias.item())

test_x = torch.Tensor([[4.0]])
test_y = model(test_x)
print('y_pred=', test_y.item())

plt.plot(range(100), Loss)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()
