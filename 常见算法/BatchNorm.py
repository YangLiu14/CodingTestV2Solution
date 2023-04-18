import numpy as np


class BatchNorm2D():
    gamma, beta = 1, 0  # 缩放因子γ和平移因子β，能训练的参数

    def __init__(self, channel, momentum=0.1, eps=1e-5):
        self.running_mean = np.zeros(channel)  # 用于测试时
        self.running_var = np.ones(channel)  # 同上
        self.momentum = momentum
        self.eps = eps  # 接近于0的数，用于避免分母为0
        self.training = True

    def forward(self, input):
        # input.shape: (B, C, H, W)
        len_ch = input.size(1)
        output = np.zeros(input.size())

        for i in range(len_ch):
            in_ch = input[:, i, :, :]
            total_elem = in_ch.numel()

            if self.training:
                # 计算均值和方差，并归一化
                mean = in_ch.sum() / total_elem
                var = ((in_ch - mean) ** 2).sum() / total_elem
                out_ch = (in_ch - mean) / (var + self.eps) ** 0.5  # 归一化

                # 更新参数
                var_unbiased = ((in_ch - mean) ** 2).sum() / (total_elem - 1)
                self.running_mean[i] = self.running_mean[i] * (1 - self.momentum) + mean * self.momentum
                self.running_var[i] = self.running_var[i] * (1 - self.momentum) + var_unbiased * self.momentum
            else:
                out_ch = (in_ch - self.running_mean[i]) / (self.running_var[i] + self.eps) ** 0.5

            out_ch = self.gamma * out_ch + self.beta  # 缩放平移
            output[:, i, :, :] = out_ch

        return output
