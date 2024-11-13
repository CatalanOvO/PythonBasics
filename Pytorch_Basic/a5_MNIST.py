import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision import datasets

train_set = datasets.MNIST(root='../dataset/mnist', train=True, transform=transforms.ToTensor(),
                           download=True)
# datasets中拿出来的数据是用PIL(Python Image Library)读出来的, 所以需要把转化成张量
test_set = datasets.MNIST(root='../dataset/mnist', train=False, transform=transforms.ToTensor(),
                          download=True)

train_loader = DataLoader(dataset=train_set, batch_size=32, shuffle=True)
test_loader = DataLoader(dataset=test_set, batch_size=32, shuffle=False)
# 在测试的时候, 由于这个模型没有改变的, 所以不做shuffle(使得每次输出测试样本的预测, 顺序是一样的, 这对观测有帮助)

