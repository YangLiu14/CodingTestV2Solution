__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


from typing import List, Dict

#####################################################
# Leetcode 15
# 给一个数组和一个target k，找出数组中有满足条件且不重复的三元组，
# 满足 a+b+c = target

# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，target = 0
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#####################################################


def print_unique_triad(arr: List[int], target: int):
    if not arr or len(arr) < 3:
        return

    # 以下的逻辑全都是基于有序数组
    arr.sort()

    for i in range(len(arr) - 2):
        # 先确定三个数中的第一个数
        if i == 0 or arr[i] != arr[i-1]:
            # 然后开始看后面两个数字的组合
            print_rest(arr, i, i+1, len(arr)-1, target - arr[i])


def print_rest(arr: List[int], anchor, l, r, target):
    while l < r:
        if arr[l] + arr[r] < target:
            # 和小于target，说明左边的数字太小了，l向右移动
            l += 1
        elif arr[l] + arr[r] > target:
            # 和大于target，说明右边的数字太大了，r向右移动
            r -= 1
        else:
            if l == anchor + 1 or arr[l-1] != arr[l]:
                print(str(arr[anchor]) + ", " + str(arr[l]) + ", " + str(arr[r]))
            l += 1
            r -= 1


if __name__ == "__main__":
    arr1 = [-8, -4, -3, 0, 1, 2, 4, 5, 8, 9]
    print_unique_triad(arr1, target=10)

