"""iou.py: basic IoU calculation with PyTorch"""
__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"

import torch


def intersect(box_a, box_b):
    """
    Args:
        box_a: (tensor) shape (A, 4)
        box_b: (tensor) shape (B, 4)

    Returns:
        (tensor) intersection area, shape (A, B)
    """
    A = box_a.size(0)
    B = box_b.size(0)

    #                   (A, 4) -> (A, 1, 4) -> (A, B, 2)
    max_xy = torch.min(box_a[:, 2:].unsqueeze(1).expand(A, B, 2),
                       box_b[:, 2:].unsqueeze(0).expand(A, B, 2))  # (A, B, 2)
    min_xy = torch.max(box_a[:, :2].unsqueeze(1).expand(A, B, 2),
                       box_b[:, :2].unsqueeze(0).expand(A, B, 2))
    inter = torch.clamp((max_xy - min_xy), min=0)
    return inter[:, :, 0] * inter[:, :, 1]


def jaccard(box_a, box_b):
    inter = intersect(box_a, box_b)  # (A, B)
    area_a = (box_a[:, 2] - box_a[:, 0]) * (box_a[:, 3] - box_a[:, 1])
    # (A,) -> (A, 1) -> (A, B)
    area_a = area_a.unsqueeze(1).expand_as(inter)  # (A, B)
    area_b = (box_b[:, 2] - box_b[:, 0]) * (box_b[:, 3] - box_b[:, 1])
    area_b = area_b.unsqueeze(0).expand_as(inter)
    union = area_a + area_b - inter
    return inter / union


if __name__ == '__main__':
    box_a = torch.rand((10, 4))
    box_b = torch.rand((20, 4))
    ious = jaccard(box_a, box_b)
    
