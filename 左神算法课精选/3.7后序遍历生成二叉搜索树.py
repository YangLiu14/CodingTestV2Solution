__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


from typing import List, Dict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#####################################################
# 给一个二叉搜索数的后序遍历数组，从数组中还原出二叉搜索树来
#####################################################
def postArrToBST(post: List[int]) -> TreeNode:
    if not post:
        return None

    return buildBST(post, 0, len(post)-1)

# recursive
def buildBST(post: List[int], start: int, end: int) -> TreeNode:
    # Exit Condition
    if start > end:
        return None


    head = TreeNode(post[end])
    less = -1
    more = end
    # 在当前范围内，找到比post[end]大 和 比post[end]小的两堆，求分界线
    for i in range(start, end):
        if post[end] > post[i]:
            less = i
        else:
            # 相当于more只动一次，就是从end位置来到第一个比root大的数 的位置
            more = i if more == end else more
    head.left = buildBST(post, start, less)
    head.right = buildBST(post, more, end-1)
    return head


#####################################################
# 判别一个数组是不是二叉搜索树的后序遍历结果  剑指offer 33
#####################################################
def isPostArray(arr: List[int]):
    if not arr or len(arr) == 0:
        return True

    return isPost(arr, 0, len(arr)-1)


def isPost(arr: List[int], start: int, end: int):
    if start == end:
        return True

    less = -1
    more = end
    # 尝试寻找到`比root小的一堆`和`比root大的一堆`的分界点。
    for i in range(start, end):
        if arr[end] > arr[i]:
            less = i
        else:
            more = i if more == end else more
    if less == -1 or more == end:
        # 没有左树或者右树
        # 去掉当前的头节点，继续往下查
        return isPost(arr, start, end-1)

    if less != more - 1:
        # 分界点不统一，则必然False
        return False

    # 剩下的情况，则说明 目前来说这个数组都是符合搜索二叉树后续遍历规则的
    # 继续往下检查
    return isPost(arr, start, less) and isPost(arr, more, end - 1)



if __name__ == "__main__":
    pass