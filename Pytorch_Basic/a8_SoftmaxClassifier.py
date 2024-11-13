import torch
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import DataLoader
import torch.nn.functional as F
import torch.optim as optim
# 2~4 用于构建DataLoader, 5 用于使用ReLu函数

batch_size = 64
transform = transforms.Compose([
    transforms.ToTensor(),  # 先调用它, Convert the PIL image to Tensor
    transforms.Normalize((0.1307, ), (0.3081, ))  # 这个结果是计算所有的图像后得到的, 正则化
])
train_dataset = datasets.MNIST(root='../dataset/mnist', train=True, download=True, transform=transform)
train_loader = DataLoader(train_dataset, shuffle=True, batch_size=batch_size)
test_dataset = datasets.MNIST(root='../dataset/mnist/', train=False, download=True, transform=transform)
test_loader = DataLoader(test_dataset, shuffle=False, batch_size=batch_size)

