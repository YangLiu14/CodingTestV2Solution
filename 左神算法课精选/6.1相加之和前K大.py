__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"

import tqdm
from typing import List, Dict

#####################################################
# 给两个数组 arr1, arr2, 分别从数组1，2中取两个数字相加，
# 求相加之和的第K大的数字

# 例：arr1 = [3, 6, 9, 12], arr2 = [6, 8, 11], k=3
# top1 = 23 = 12+11
# top2 = 20 = 12+8
# top3 = 20 = 9+11

# 输出20
#####################################################


import heapq