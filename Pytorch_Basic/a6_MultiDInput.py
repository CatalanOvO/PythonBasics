import numpy as np
import torch
from sklearn.model_selection import train_test_split


xy = np.loadtxt('diabetes.csv', delimiter=',', dtype=np.float32)
x_data = torch.from_numpy(xy[:, :-1])  # 所有行, 列取倒数第n列到倒数第2列(不包含倒数第一列)
y_data = torch.from_numpy(xy[:, [-1]])  # [-1]用中括号表示只选择最后一列, 并保持二维数组的形式. 这通常用于选择目标值列。
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=42)


class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)
        self.sigmoid = torch.nn.Sigmoid()
        # self.activate = torch.nn.ReLU()
        # 这里用的是nn中的Sigmoid, 这是一个模块, 没有参数(这里实例化一个对象作为一层)
        # nn.functional中的sigmoid是一个函数

    def forward(self, x):
        x = self.sigmoid(self.linear1(x))  # 实际上这里分别是 o1= , o2= , y_hat=
        x = self.sigmoid(self.linear2(x))  # 但是为了避免写错, debug很麻烦, 所以就用x来迭代
        x = self.sigmoid(self.linear3(x))
        return x


model = Model()

criterion = torch.nn.BCELoss(reduction='mean')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(100):
    # 注:这里取的不是Mini-Batch
    y_pred = model(x_train)
    loss = criterion(y_pred, y_train)
    print(f'Epoch {epoch + 1}/100, Loss: {loss.item():.4f}')  # 输出损失

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# # 使用模型进行测试
# with torch.no_grad():  # 测试时不需要计算梯度
#     y_test_pred = model(x_test)  # 对测试集进行预测
#     test_loss = criterion(y_test_pred, y_test)  # 计算测试集上的损失
#     print(f'Test Loss: {test_loss.item():.4f}')  # 输出测试集损失
#
# # 额外：如果想要查看预测结果和真实标签，可以打印它们
# print("Predicted values (sigmoid output):", y_test_pred)
# print("True labels:", y_test)
