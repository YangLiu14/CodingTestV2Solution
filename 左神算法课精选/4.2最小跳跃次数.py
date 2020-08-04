__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


from typing import List, Dict
#####################################################
# 给一个数组，数组i位置的数，表示小球可以跳到的最远位置。

# 例子1：
# jump = [2, 5, 1, 1, 1, 1]
# 输出2。解释：先从0位置，可以跳两步，跳到1位置，可以跳五步，直接跳出


# 解法：只要遍历一次数组，每遍历一个位置就扩大我的右边界，并且同时记录
# 上一次左边界的位置，如果遍历超过了上一次左边界，则jump的步数+1，然后更新左边界
#####################################################
def jump(self, arr: List[int]) -> int:
    if not jump:
        return

    curr_limit = 0
    max_reach = 0
    count = 0  # count the number of times we jump
    for i in range(len(jump)):
        if i > curr_limit:
            count += 1
            curr_limit = max_reach
        max_reach = max(max_reach, i + jump[i])
    return count


#####################################################
# https://leetcode-cn.com/problems/zui-xiao-tiao-yue-ci-shu/
# LeetCode LCP 09. 最小跳跃次数
# 当 i + jump[i] >= N 表示成功跳出
# LeetCode这题和上面的区别在于：
# 1. 可以左跳到任意之前到过的位置（即 0~i-1)
# 2. 但是如果右跳，那就只能固定跳当前所在的位置所能跳的步数 jump[i]

# 例子1：
# jump = [2, 5, 1, 1, 1, 1]
# 输出3。解释：先右跳到2位置，回跳到1位置，可以跳五步，直接跳出

#####################################################
class Solution:
    def minJump(self, jump: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    arr0 = [2,5,1,1,1,1]
    arr1 = [3,7,6,1,4,3,7,8,1,2,8,5,9,8,3,2,7,5,1,1]
    arr2 = [4,6,10,8,3,5,3,5,7,8,6,10,3,7,3,10,7,10,10,9,1,4,7,4,8,6,9,8,8,2,7,2,4,5,4,3,3,2,2,2,3,4,4,1,1,5,6,8,1,2]

    print(sol.minJump(arr1))
