import torch
import numpy as np
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from a6_MultiDInput import Model
# Dataset 是一个抽象类, 不能实例化
# DataLoader是可以实例化的


class DiabetesDataset(Dataset):
    def __init__(self, filepath):
        # 做一些初始化, 可能不加载所有数据
        # 为了保证内存的高效使用, 把y放入一个列表中, 然后要读的时候读出第i个
        xy = np.loadtxt(filepath, delimiter=',', dtype=np.float32)
        self.len = xy.shape[0]  # 原数据集是一个 N*9 的矩阵, 这里获取样本个数
        self.x_data = torch.from_numpy(xy[:, :-1])
        self.y_data = torch.from_numpy(xy[:, [-1]])

    def __getitem__(self, index):  # magic function, 要求实例化之后可以下标操作
        return self.x_data[index], self.y_data[index]  # 返回的是(x,y)

    def __len__(self):  # magic function, 求数量
        return self.len


if __name__ == '__main__':
    dataset = DiabetesDataset('diabetes.csv')
    train_loader = DataLoader(dataset=dataset, batch_size=32, shuffle=True, num_workers=2)

    model = Model()
    criterion = torch.nn.BCELoss(reduction='sum')
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(100):
        for i, data in enumerate(train_loader, 0):
            # 1 Prepare data
            inputs, labels = data  # 这里inputs和labels都是张量
            # 2 Forward
            y_pred = model(inputs)
            loss = criterion(y_pred, labels)
            print(epoch, i, loss.item())
            # 3 Backward
            optimizer.zero_grad()
            loss.backward()
            # 4 Update
            optimizer.step()

