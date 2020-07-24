__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


from typing import List, Dict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


###############################################
# 最大路径和：
# 可以树中的任意一个节点出发，只能往下走，也可以随时停止。
# 求所形成的 最大的路径和
###############################################
class Info1:
    def __init__(self, m, f):
        # 树中最大的路径和
        self.maxPathSum = m
        # 树中最大的，且从head出发的路径和
        self.fromHeadPathSum = f


def maxPathSum(head: TreeNode):
    if not head:
        return 0

    res = maxPathSum_core(head)
    return res.maxPathSum

INT_MIN = 2e-31
def maxPathSum_core(node: TreeNode):
    if not node:
        return None

    # 获取左右子树的信息
    leftInfo = maxPathSum_core(node.left)
    rightInfo = maxPathSum_core(node.right)

    # 情况一：和当前node没有关系，只是把左右子树的信息传递上来
    p1 = INT_MIN
    if leftInfo:
        p1 = leftInfo.maxPathSum
    p2 = INT_MIN
    if rightInfo:
        p2 = rightInfo.maxPathSum

    # 情况二：和当前node有关系，左右子树的信息和node整合起来
    p3 = node.val
    p4 = INT_MIN
    if leftInfo:
        p4 = node.val + leftInfo.fromHeadPathSum
    p5 = INT_MIN
    if rightInfo:
        p5 = node.val + rightInfo.fromHeadPathSum

    maxPathSum = max(p1, p2, p3, p4, p5)
    fromHeadMaxPathSum = max(p3, p4, p5)

    return Info1(maxPathSum, fromHeadMaxPathSum)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)

    print(maxPathSum(root))