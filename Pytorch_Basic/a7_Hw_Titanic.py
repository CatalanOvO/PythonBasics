import torch
import numpy as np
from torch.utils.data import DataLoader
from torch.utils.data import Dataset


class TitanicDataset(Dataset):
    def __init__(self, filepath, is_train=True):
        xy = np.loadtxt(filepath, delimiter=',', dtype=str)
        self.len = xy.shape[0]
        if is_train:
            self.x_data = torch.from_numpy(xy[:, [2, 3, 4, 5, 6, 7, 9]])
            self.y_data = torch.from_numpy(xy[:, [1]].astype(np.float32))
        else:
            self.x_data = torch.from_numpy(xy[:, 1:])
            self.y_data = None
        mapping1 = {'male': 0, 'female': 1}
        self.x_data[:, 1] = np.vectorize(mapping1.get)(self.x_data[:, 1])
        mapping2 = {'S': 0, 'C': 1, 'Q': 0}
        self.x_data[:, 6] = np.vectorize(mapping2.get)(self.x_data[:, 6])
        new_column = np.where(xy[:, 7] == 'Q', 1, 0).astype(np.float32)
        self.x_data = np.column_stack((self.x_data, new_column))

        self.x_data = torch.from_numpy(self.x_data.astype(np.float32))

    def __getitem__(self, index):
        if self.y_data is not None:
            return self.x_data[index], self.y_data[index]
        else:
            return self.x_data[index]  # 测试集没有 y_data

    def __len__(self):
        return self.len


class ClassifyModel(torch.nn.Module):
    def __init__(self):
        super(ClassifyModel, self).__init__()
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        x = self.sigmoid(self.linear3(x))
        return x


if __name__ == '__main__':
    train_dataset = TitanicDataset('../dataset/Titanic/train.csv')
    train_dataset = TitanicDataset('../dataset/Titanic/train.csv', False)
    train_set = DataLoader(dataset=train_dataset, batch_size=32, shuffle=True, num_workers=2)
    test_set = DataLoader(dataset=train_dataset, batch_size=32, shuffle=False, num_workers=2)

    model = ClassifyModel()
    criterion = torch.nn.BCELoss(reduction='avg')
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(1000):
        for i, (x, y) in enumerate(train_set):
            y_pred = model(x)
            loss = criterion(y_pred, y)
            print(epoch, i, loss.item())

            optimizer.zero_grad()
            loss.backward()

            optimizer.step()




