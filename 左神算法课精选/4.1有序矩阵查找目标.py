__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


from typing import List, Dict


#####################################################
# Leetcode 378. 有序矩阵中第K小的元素

# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# 返回 13。
#####################################################
#####################################################
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/

# 思路: 二分法
# 把左边界设为矩阵中的最小值(0,0)处，把右边界设为矩阵中的最大值
# mid 相当于中间位置，对角线附近的区域
#
# 接下来就从左下角的格子开始走，直接碰到mid这条分割线，
# 每向右走一步就把这一列的所有数字统计起来，看有没有超过k
# 超过k说明mid选大了，没超过说明选小了。
#####################################################
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            # 从matrix的左下角开始出发
            i, j = n-1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    # 当前格子的数字比mid小，想要大一点，于是向右移动一格
                    num += i + 1 # 把这一列的数字都加上
                    j += 1
                else:
                    # 当前格子的数字比mid大，想要小一点，于是向左移动一格
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left



if __name__ == "__main__":
    matrix1 = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15]
             ]
    matrix2 = [[1,2],[1,3]]

    sol = Solution()
    # print(sol.kthSmallest(matrix1, k=8))  # print 13
    print(sol.kthSmallest(matrix2, k=2))  # print 1
