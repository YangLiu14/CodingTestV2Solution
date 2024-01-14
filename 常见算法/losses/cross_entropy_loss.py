"""
----------------------------------------
<<< Binary Cross-Entropy Loss >>>

H(y, p) = - \sum_{i} { yi*log(pi) + (1 - yi)*log(1 - pi) }
----------------------------------------

----------------------------------------
<<< Multi-class Classification Loss >>>å
H(y, p) = - \sum_{i}\sum_{c} { y_{i,c}*log(p_{i,c}) }

y_{i, c} = 1, when i==c
i的是i个数据
c是class的数量
----------------------------------------

"""
import numpy as np


# Forward
def binary_cross_entropy_loss(y_true, y_pred):
    eps = 1e-15
    y_pred = np.clip(y_pred, eps, 1 - eps)  # clip prediction to avoid log(0)
    loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return loss


# Backward
def BCE_backward(y_true, y_pred):
    # https://juejin.cn/s/binary%20cross%20entropy%20loss%20gradient
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    gradient = (y_pred - y_true) / (y_pred * (1 - y_pred))
    return gradient


# Forward
def multiclass_cross_entropy_loss(y_true, y_pred):
    """
    Args:
        y_true: one-hot encoded numpy array, shape = (N, n_classes)
        y_pred: predicted probs, shape = (N, n_classes)
    """
    eps = 1e-15
    y_pred = np.clip(y_pred, eps, 1 - eps)  # clip prediction to avoid log(0)
    loss = -np.mean(np.sum(y_true * np.log(y_pred), axis=1))
    return loss


# Backward
def CE_backward(y_true, y_pred):
    # https://blog.csdn.net/jiongjiongai/article/details/88324000
    gradient = y_pred - y_true
    return gradient


if __name__ == '__main__':
    # Binary classification
    y_true_binary = np.array([0, 1, 0, 1])
    y_pred_binary = np.array([0.1, 0.9, 0.2, 0.8])
    binary_loss = binary_cross_entropy_loss(y_true_binary, y_pred_binary)

    # Multi-class classification
    y_true_categorical = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0]])
    y_pred_categorical = np.array([[0.7, 0.2, 0.1], [0.1, 0.8, 0.1], [0.2, 0.2, 0.6], [0.9, 0.05, 0.05]])
    categorical_loss = multiclass_cross_entropy_loss(y_true_categorical, y_pred_categorical)

    print("Binary Cross-Entropy Loss:", binary_loss)
    print("Categorical Cross-Entropy Loss:", categorical_loss)
