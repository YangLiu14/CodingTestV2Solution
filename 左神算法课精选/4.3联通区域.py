__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


from typing import List, Dict
#####################################################
# 给一个不包含1的正数数组，规定任意两个数字之间如果有除了1的公约数
# 则说这两个数构成一个联通区域。
# 求给定数组中一共有多少联通区域，以及最大的联通区域内有多少数字。


# 例1：
# arr = [7, 3, 5]
# 一共3个联通区域，最大的联通区域只有1个数字

# 例2：
# arr = [7, 3, 5, 15]
# 一共2个联通区，最大的联通区域有3个数字 (3,5,15)
#####################################################
# ===================================================
# 本题使用了并查集的概念
# ===================================================
from data_structure.UnionFindSet import UnionFindSet

def largest_connected_area(arr: List[int]):
    # 并查集初始化
    uset = UnionFindSet(arr)
    # 两两数字比较，看是否有最大公约数
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if gcd(arr[j], arr[i]) != 1:
                # 如果有最大公约数，则把两个数字合并到并查集的同一个集合里
                uset.union(arr[j], arr[i])

    return uset.num_sets(), uset.max_size()


def gcd(num1: int, num2: int) -> int:
    """
    Greatest Common Divisor. 返回两个数字的最大公约数
    """
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


if __name__ == "__main__":
    print(largest_connected_area([7, 3, 5, 15]))  # output (2, 3)
    # print(largest_connected_area([7, 3, 5, 15, 15]))  # output 3 缺点：不能有重复数字。解决方案，可以存储下标
    print(largest_connected_area([7, 3, 5, 15, 21]))  # output (1, 5)
    print(largest_connected_area([2, 3, 6, 7, 4, 12, 21, 39]))  # output (1, 8)

