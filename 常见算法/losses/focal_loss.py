"""
Focal loss

FL(pt) = - \alpha * (1 - pt)^{\gamma} * log(pt)
"""
import numpy as np


class FocalLoss:
    def __init__(self, alpha=0.25, gamma=2.0):
        self.alpha = alpha
        self.gamma = gamma

    def forward(self, y_true, y_pred):
        eps = 1e-15
        y_pred = np.clip(y_pred, eps, 1 - eps)
        pt = y_true * y_pred + (1 - y_true) * (1 - y_pred)
        alpha_t = y_true * self.alpha + (1 - y_true) * (1 - self.alpha)
        loss = -np.mean(alpha_t * (1 - pt)**self.gamma * np.log(pt))
        return loss

    def backward(self, y_true, y_pred):
        eps = 1e-15
        y_pred = np.clip(y_pred, eps, 1 - eps)
        pt = y_true * y_pred + (1 - y_true) * (1 - y_pred)
        alpha_t = y_true * self.alpha + (1 - y_true) * (1 - self.alpha)

        gradient = -alpha_t * np.power(1 - pt, self.gamma - 1) * (
                self.gamma * pt * np.log(pt) + pt - 1
        )
        gradient = gradient * (y_true * (1 / y_pred) + (1 - y_true) * (-1 / (1 - y_pred)))
        return gradient


if __name__ == '__main__':
    focal_loss = FocalLoss()
    y_true_binary = np.array([0, 1, 0, 1])
    y_pred_binary = np.array([0.1, 0.9, 0.2, 0.8])
    focal_loss_value = focal_loss.forward(y_true_binary, y_pred_binary)
    focal_loss_grad = focal_loss.backward(y_true_binary, y_pred_binary)

    print("Focal Loss Value:", focal_loss_value)
    print("Focal Loss Gradient:", focal_loss_grad)
