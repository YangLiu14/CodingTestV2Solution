__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


from typing import List, Dict
from data_structure.UnionFindSet import UnionFindSet

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#####################################################
# 剑指offer 68 二叉树的最近公共祖先
#####################################################
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Exit condition
        if not root:
            # 简单返回上一级函数
            return
        if root == p or root == q:
            # 碰到了我们需要找的节点中的任意一个，不用再继续往深了走了，回到上一级
            return root

        # Go all the way left, 直到没有子树，或者遇到了p或者q
        left = self.lowestCommonAncestor(root.left, p, q)
        # 向右走一步，
        right = self.lowestCommonAncestor(root.right, p, q)

        # 运行到这的时候，有几种情况
        # 1. 左右都遍历到了None的时候，直接返回上一级函数
        if not left and not right:
            return
        # 2. 只有左边找到了p位置，此时 left == p
        if not right:
            return left
        # 3. 只有右边找到了q位置，此时 right == q
        if not left:
            return right
        if left and right:
            return root  # 找到了答案


if __name__ == "__main__":
    pass