"""playground.py: playground for python coding test"""
__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"

from collections import Counter, defaultdict, deque
from typing import List, Dict

# =======================
# read input
# =======================
import sys

# 反复读取一行
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)
# =========================
# End of input reading
# =========================

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#####################################
# Insert your solution there
#####################################
class Solution:
    def __init__(self):
        pass

    def your_func(self):
        pass


#####################################
# End of code
#####################################
# input: mask
# output:  count,  bboxs

if __name__ == "__main__":

    sol = Solution()

    ###################################
    # 测试模块
    ###################################

    ###################################
    # END of 测试模块
    ###################################




