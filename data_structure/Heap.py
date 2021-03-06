"""Heap.py"""
__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


from typing import List, Dict
"""
Heap 也被称作优先级队列

用数组表示的heap，下标在树结构中的关系
左：2*i + 1
右: 2*i + 2
父: (i-1) // 2   （默认数组下标从0开始，如果从1开始，则是i//2）
"""

#####################################
# Python heapq 使用方法
#####################################

import heapq
# ================
# min heap
# ================
minheap = [1, 2, 3, 4, 5]
heapq.heapify(minheap)
# Get current min
current_min = heapq.heappop(minheap)
# Push a new number
heapq.heappush(minheap, 10)

# ================
# max heap
# ================
maxheap = [1, 2, 3, 4, 5]
heapq._heapify_max(maxheap)
# Get current max
current_max = heapq._heappop_max(maxheap)
# Push a new number, and rearrange as maxheap
heapq.heappush(maxheap, 10)
heapq._heapify_max(maxheap)

#####################################
# END of Python heapq 使用方法
#####################################


#####################################
# MAX HEAP 手动实现
#####################################
def heapInsert(arr: List, index: int):
    """在表示max-heap的数组中的index位置插入一个数字。
    整理方法是，不断将当前index的数字和它父节点的数字比较，如果比父节点大，则交换位置

    :param arr: 插入新数值之后的数组
    :param index: 新数值插入的位置
    """
    while arr[index] > arr[(index-1)//2]:
        arr[index], arr[(index-1)//2] = arr[(index-1)//2], arr[index]
        index = (index - 1) // 2


def heapify(arr: List, index: int, heapSize: int):
    """从index出发开始的往下的调整过程
    :param arr:
    :param index:
    :param heapSize:
    :return:
    """
    left = index * 2 + 1  # 左孩子的下标
    while left < heapSize:  # 下方还有孩子的时候
        # 左右两个孩子中，谁的值大，就把下标给largest
        if left + 1 < heapSize and arr[left + 1] > arr[left]:
            largest = left + 1  # 右孩子
        else:
            largest = left      # 左孩子

        # 父和孩子之间，谁的值大，把下标给largest
        largest = largest if arr[largest] > arr[index] else index

        if largest == index:
            break
        arr[largest], arr[index] = arr[index], arr[largest]
        index = largest
        left = index * 2 + 1


def heapSort(arr: List):
    if not arr:
        return

    # 把数组中的数一个一个用heapInsert插入进去
    for i in range(len(arr)):  # O(N)
        heapInsert(arr, i)  # O(logN)
    heapSize = len(arr)

    # 把最后一个数和头一个数交换
    arr[0], arr[heapSize - 1] = arr[heapSize - 1], arr[0]
    while heapSize > 0:  # O(N)
        heapify(arr, 0, heapSize)   # 重新组织堆  O(logN)
        heapSize -= 1
        arr[0], arr[heapSize - 1] = arr[heapSize - 1], arr[0]
    # 最后得到从大到小排列的数列
    # 整个时间复杂度 O(N logN)


if __name__ == "__main__":
    pass