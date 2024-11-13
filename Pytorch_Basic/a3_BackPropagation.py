import torch

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = torch.Tensor([1.0])
w.requires_grad = True  # 默认是False, True表示这个张量是需要计算梯度的. 只有叶子节点需要手动设置


def forward(x):
    return x * w  # 这是一个Tensors数乘, 会自动地把x转换为一个Tensor


def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) ** 2
    # 看到代码要能把计算图构建出来


print('Predict (before training):', 4, forward(4).item())

for epoch in range(100):
    for x, y in zip(x_data, y_data):
        l = loss(x, y)  # 前馈, 计算loss
        l.backward()    # 反馈, backward()计算计算图上所有requires_grad=True的张量的梯度
        '求完之后, 把梯度存到这些变量里面, 比如这里涉及到的变量是w, 梯度存到w之后, 这个计算图就被释放了'
        '下次再进行loss计算时, 会创建一个新的计算图, 因为每一次的计算图可能是不一样的！'
        print('\tgrad:', x, y, w.grad.item())  # item是标量不是Tensor
        w.data = w.data - 0.01 * w.grad.data
        '这里的张量里面存了data和grad, 而grad也是一个会计算梯度的Tensor'
        '这里如果将Tensor乘以一个值加进去, 相当于在建立计算图'
        '我们这里只希望修改w的data, 不需要构建计算图求梯度, 所以必须取到它的data(不计算梯度的Tensor)(和forward函数中不同)'

        '如果希望获取平均loss, 那我们就需要sum_loss += l.item()'
        '不能sum_loss += l , 这样会张量一直加没有backward而得不到释放, 导致内存爆炸'

        w.grad.data.zero_()
        '如果不清零, 那下一次计算L对w的偏导数会是 偏L1/偏w + 偏L2/偏w + ...'
        '有些时候需要累加, 所以需要显式清零'
    print('progress:', epoch, l.item())

print('Predict (after training):', 4, forward(4).item())
