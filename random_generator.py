"""common.py: common tools"""
__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"

import random
from typing import List, Dict


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def random_arr(low: int, high=10e5, size=100, dtype='int') -> List:
    arr = list()
    # 随机长度的array
    arr_len = random.randint(0, size)

    if dtype == 'int':
        for _ in range(arr_len):
            arr.append(random.randint(low, high))
    elif dtype == 'float':
        for _ in range(arr_len):
            arr.append(random.uniform(low, high))
    else:
        raise Exception("Choose dtype from [`int`, `float`], default is `int`")

    return arr


def random_ListNode(size: int) -> ListNode:
    low = 1
    high = size
    arr = random_arr(1, size, size=size, dtype='int')


def random_Tree():
    pass


def random_2x2matrix():
    pass
