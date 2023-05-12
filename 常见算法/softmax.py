import numpy as np
import torch
import torch.nn as nn


# Simple version
def softmax(x, dim=1):
    """
    Args:
        x (tensor), shape=(B, C)
    """
    assert(len(x.shape) == 2)
    row_max = np.max(x, axis=dim).reshape(-1, 1)  # (B, 1)
    x -= row_max
    x_exp = np.exp(x)
    return x_exp / np.sum(x_exp, axis=dim, keepdims=True)


class Softmax:
    def __init__(self, dim=0):
        self.dim = dim
        self.res = None

    def forward(self, x):
        """
            Args:
                x (tensor), shape=(B, C)
        """
        assert (len(x.shape) == 2)
        row_max = np.max(x, axis=self.dim).reshape(-1, 1)  # (B, 1)
        x -= row_max
        x_exp = np.exp(x)
        self.res = x_exp / np.sum(x_exp, axis=self.dim, keepdims=True)
        return self.res  # (B, C)

    def backward(self, grad):
        """
        Derivative: sig(x)(1 - sig(x))  with sig(x) is actually softmax(x)
        """
        d = self.res * np.identity(self.res.size) - self.res.transpose() @ self.res
        return grad @ d

"""
如果loss func使用Cross Entropy：L = - \sum_{i=1}^{n} {y_i * ln(a_i)}  a_i 是 softmax_i
那么求导的结果直接是 a - y (a和y是向量) 

具体推导过程可见：https://www.zhihu.com/tardis/zm/art/105758059?source_id=1003
"""


if __name__ == '__main__':
    x = np.random.rand(4, 12)
    res1 = softmax(x)

    # Compare with
    x = torch.from_numpy(x)
    torch_softmax = nn.Softmax(dim=1)
    res2 = torch_softmax(x).numpy()

    print(np.all((res1 - res2) < 0.001))

