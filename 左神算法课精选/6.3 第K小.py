__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"

import warnings
from typing import List, Dict

#####################################################
# 给一个无序数组，返回里面第K大的数字
#####################################################

####################################################
# 思路1：利用快排中的partition
# 1. 在[L .. R]上随机选择一个P
# 2. partition过程之后，数组被分割成三块
#    [小于P，等于P，大于P]
# 3. 如果"等于P"部分下标正好包括了k，返回
#    否则，在左侧继续递归，或者在右侧继续递归

# 时间复杂度为 O(N) （平均情况收敛到这个复杂度）
#####################################################


####################################################
# 思路2：BFPRT算法——在思路1的基础上，在第一步进行优化
# 1.1 根据k的大小，给arr分组。比如arr长度为14，k=5，
#     那就5个数一组这么分，分成 5 5 4
# 1.2 求出每一组中的上中位数
# 1.3在所有中位数组成了一个新数组，这个新数组的长度是 len(arr) // N，取新数组中的上中位数


# 2. partition过程之后，数组被分割成三块
#    [小于P，等于P，大于P]
# 3. 如果"等于P"部分下标正好包括了k，返回
#    否则，在左侧继续递归，或者在右侧继续递归

# 时间复杂度为 O(N)


## 分析：为什么费这么大的劲去选取第一步的pivot？
# 是为了让P尽量分布在数组的中间位置，这样递归再往左或者再往右走，
# 左右两个数组不至于过于大。
# https://zhuanlan.zhihu.com/p/31498036
#####################################################


def get_min_Kth_BFPRT(arr: List[int], k: int):
    arr_copy = arr.copy()
    return select(arr_copy, 0, len(arr_copy) - 1, k-1)


# 算法主体
def select(arr: List[int], begin: int, end: int, i: int):
    """
    在arr[begin ... end]范围上，如果arr排序（从小到大），求index i上的数字是什么
    :param arr: 无序数组
    :param begin: 起始index
    :param end: 终止index
    :param i: query index
    :return: int
    """
    if begin == end:
        return arr[begin]

    # Step 1: 用BFPRT的方式选择pivot
    pivot = median_of_medians(arr, begin, end)

    # Step 2: 根据pivot进行划分， <p  ==p  >p
    # 返回"等于"区的左右边界
    pivot_range = partition(arr, begin, end, pivot)

    # Step 3: 决定下一次递归的方向，（选左半边数组还是右半边）
    if pivot_range[0] <= i <= pivot_range[1]:
        # 正好在"等于"区
        return arr[i]
    elif i < pivot_range[0]:
        return select(arr, begin, pivot_range[0]-1, i)
    else:  # i > pivot_range[1]
        return select(arr, pivot_range[1]+1, end, i)


def median_of_medians(arr: List[int], begin: int, end: int):
    length = end - begin + 1
    offset = 0 if length % 5 == 0 else 1
    # 分组
    m_arr = [0] * (length // 5 + offset)
    for i in range(len(m_arr)):
        begin_i = begin + i*5
        end_i = begin_i + 4
        m_arr[i] = get_median(arr, begin_i, min(end_i, end))

    # 一直细分，找到中位数数组的中位数，直到数组中只有一个数，作为主程序中的pivot
    return select(m_arr, 0, len(m_arr) - 1, len(m_arr) // 2)


def get_median(arr: List[int], begin: int, end: int):
    insertion_sort(arr, begin, end)
    sum = end + begin
    mid = (sum // 2) + (sum % 2)  # 后面加的是考虑了数组长度为奇数或者为偶数的 offset
    return arr[mid]


def insertion_sort(arr: List[int], begin: int, end: int):
    for i in range(begin + 1, end + 1):
        for j in reversed(range(begin + 1, i + 1)):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break


def partition(arr: List[int], begin: int, end: int, pivot: int):
    small = begin - 1  # 比pivot小的数字的index疆界
    curr = begin
    big = end + 1  # 比pivot大的数字的index疆界
    while curr != big:
        if arr[curr] < pivot:
            small += 1
            arr[curr], arr[small] = arr[small], arr[curr]
            curr += 1
        elif arr[curr] > pivot:
            big -= 1
            arr[big], arr[curr] = arr[curr], arr[big]
        else:
            curr += 1

    range = [0] * 2
    range[0] = small + 1
    range[1] = big - 1
    return range


if __name__ == "__main__":
    arr = [6, 9, 1, 3, 1, 2, 2, 5, 6, 1, 3, 5, 9, 7, 2, 5, 6, 1, 9]
    print(get_min_Kth_BFPRT(arr, 10))

    # Test
    arr.sort()
    print(arr[9])
