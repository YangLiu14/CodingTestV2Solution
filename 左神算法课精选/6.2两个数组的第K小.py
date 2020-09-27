__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"

import warnings
from typing import List, Dict

#####################################################
# 给两个升序数组 arr1, arr2, 数组长度分别为N, M
# 求arr1 和 arr2 两个数组合起来时，第K小的数字

# 例：arr1 = [3, 6, 9, 12], arr2 = [1, 7, 8, 11], k=3
# 输出6
#####################################################

#####################################################
# 思路：
# 最优解可以做到 O(log(min{N, M}))

    # ==========================================
    # 一：让我们先考虑一个理想情况：
    #     arr1和arr2等长, 长度为偶数
    #     如何找到两个数组整体的中位数
    # 例子：arr1 = [n1, n2, n3, n4]
    #      arr2 = [m1, m2, m3, m4]
    # 二者各自的中位数是n2, m2，
    ## 如果n2 = m2，则合并数组的中位数就是n2（或者m2）

    ## 如果n2 > m2，那么整体的中位数（第4个数）将会出现在
    # [n1, n2], [m3, m4]中。
    # 注意，到此我们又得到了两个等长升序数组
    # 这就可以愉快用递归了。
    #

    # 二：arr1和arr2等长，长度为奇数
    # 例子：arr1 = [n1, n2, n3, n4, n5]
    #      arr2 = [m1, m2, m3, m4, m5]
    # 二者各自的中位数是n3, m3
    ## 如果 n3 = m3, 则合并数组的中位数就是n3（或者m3）

    ## 如果n3 > m3，那么整体的中卫数（第5个数）将会出现在
    # [n1, n2], [m3, m4, m5]
    # 这时发现得到的不是等长的数组了，怎么办？
    ### 这时候可以验证一下 n2和m3的大小
    ### 如果 m3 >= n2，直接说明了m3是整体第五大的数字，return m3
    ### 如果 m3 < n2，m3至少是第六个数，把m3去掉，
    # 这样我们又得到了等长数组，可以继续递归。
    # ==========================================

# 以上是对理想情况的理解，相当于现在我们有了一个baseline。
# 现在就考虑，如何把两个不等长数组，转化为上述的情况。
# 比如 arr1的长度 N=10, arr2的长度 M=17

# ====================================================
## 情况1：当 1 <= k <= min(N, M)
# 那么arr1取前k个，arr2取前k个，作为我们的两个等长数组求解即可。

# =====================================================
## 情况2：当 max(N, M) <= k <= N + M，比如 k=23
# 例子：arr1 = [n1, ..., n10], N=10; arr2 = [m1, ..., m17], M=17
# arr1中，n6之前的五个数，都不可能是第23小的数，因为 5+17 < 23
# arr2中，m13之间的12个数，都不可能是第23小的数，因为10+12 < 23
# 此时我们一共淘汰了17个数字，
#       arr1中剩下 n6~n10 五个数, arr2中剩下，m13~m17 五个数
#       如果我们在这剩下的10个数中求第五小（中位数），
#       那么17+5我们找到的实际上是第22个数， 而要求的k=23
# 因此我们需要继续缩小剩下的数组的长度：
#       1. 剔除n6：如果n6 >= m17，直接renturn n6；不然n6可以剔除
#       2. 剔除m13：如果m13 >= n10, 直接return m13，否则剔除

# =====================================================
## 情况3：当 min(N, M) <= k <= max(N, M)
# 例子：arr1 = [n1, ..., n10], N=10; arr2 = [m1, ..., m17], M=17
#      k = 15
# 那么arr1中所有数都有可能是最终答案，都保留
# arr2中，m5之间的4个数字都不可能，10+4 < 15; m15之后的2个数不可能 16 > 15;
# 于是arr1保留了 n1~n10 十个数，arr2保留了 m5~m15 11个数字
# 我们可以用类似的思想剔除m5，得到10 + 10的两个数组。日9一67


def find_Kth_num_in_two_arrays(arr1: List[int], arr2: List[int], k: int):
    if not arr1 or not arr2:
        warnings.warn("Invalid input arrays")
    if k < 1 or k > len(arr1) + len(arr2):
        warnings.warn("Invalid k")

    # 保证arr1永远是较长的那个数组
    if len(arr2) > len(arr1):
        arr1, arr2 = arr2, arr1

    N, M = len(arr1), len(arr2)

    if k <= M:
        return get_up_median(arr2, 0, k - 1, arr1, 0, k - 1)

    if k > N:
        # 剔除一些数据，使得两个数组剩下的数据是等长的
        if arr2[k - N - 1] >= arr1[N - 1]:
            return arr2[k - N - 1]
        if arr1[k - M - 1] >= arr2[M - 1]:
            return arr1[k - M - 1]

        return get_up_median(arr2, k - 1, M - 1, arr1, k - M, N - 1)

    if arr1[k - M - 1] >= arr2[M - 1]:
        return arr1[k - M - 1]

    return get_up_median(arr2, k - N, M - 1, arr1, k - M, N - 1)


def get_up_median(arr1: List[int], s1: int, e1:int, arr2: List[int], s2: int, e2: int):
    """
    求两个等长的有序数组 组合起来之后的上中位数，两个数组长度必须一样。
    :param arr1:
    :param s1: arr1的第一个元素index
    :param e1: arr1的最后一个元素index
    :param arr2:
    :param s2: arr2的第一个元素index
    :param e2: arr2的最后一个元素index
    :return: int
    """
    assert e1 - s1 == e2 - s2
    arr1.sort()
    arr2.sort()

    while s1 < e1:
        mid1 = (s1 + e1) // 2
        mid2 = (s2 + e2) // 2
        offset = ((e1 - s1 + 1) & 1) ^ 1  # 这个表达式，奇数输出1，偶数输出0

        if arr1[mid1] > arr2[mid2]:
            e1 = mid1
            s2 = mid2 + offset
        elif arr1[mid1] < arr2[mid2]:
            s1 = mid1 + offset
            e2 = mid2
        else:
            return arr1[mid1]

    return min(arr1[s1], arr2[s2])







