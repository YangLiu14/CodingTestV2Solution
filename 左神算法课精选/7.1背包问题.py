__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"

import warnings
from typing import List, Dict

#####################################################
# 背包问题1：
# 往背包里放入一些物品，背包的总容量是C
# 一共n个物体，第i个物品的体积为w[i]
# 请问在总体积不超过背包容量的情况下，一共有多少种零食放法
# （总体积为0也算是一种放法）
#####################################################


# 递归方法
def ways_put_in_bag1(items: List[int], C: int):
    return recursive1(items, 0, C)


def recursive1(items: List[int], index: int, rest: int) -> int:
    """
    items: 物品列表
    index: 目前还能在物品列表中，从index开始的地方开始选择物品放入背包
    rest: 背包目前还剩下的容量

    return: int
        返回选择的方案数
    """
    # Exit condition
    if rest < 0:  # 没容量了
        return -1 # 表示无方案

    if index == len(items):  # 无物品可选了，只有一种方案
        return 1

    # Main body
    next1 = recursive1(items, index + 1, rest)  # index号零食不放入背包
    next2 = recursive1(items, index + 1, rest - arr[index])  # index号零食放入背包
    if next2 == -1:
        next2 = 0
    return next1 + next2  # 返回两种方案的累加


# 动态规划
#dp[i][j] 表示items中 0～i号物品自由选择，但是凑出来的体积必须严格等于j

def ways_put_in_bag2(items: List[int], C: int):
    N = len(items)
    dp = [[0] * (C+1) for _ in range(N)]
    # init
    for i in range(0, N):
        dp[i][0] = 1  # 当背包为0容量时，自然只能选择“不放”这一种方案
    if arr[0] <= C:
        dp[0][arr[0]] = 1

    # Update dp
    for i in range(1, N):
        for j in range(1, C+1):
            if j - arr[i] >= 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i]]
            else:
                dp[i][j] = dp[i-1][j] + 0

    ans = 0
    for j in range(0, C+1):
         ans += dp[N-1][j]  # 把所有符合条件的（背包容量小于C的方案）都加起来

    return ans


if __name__ == "__main__":
    arr = [4, 3, 2, 9]
    C = 8
    print(ways_put_in_bag1(arr, C))
    print(ways_put_in_bag2(arr, C))
