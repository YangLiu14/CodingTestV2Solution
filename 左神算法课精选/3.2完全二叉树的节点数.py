__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


from typing import List, Dict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


###############################################
# 给一棵"完全二叉树"，求整个树包含多少个节点
###############################################
# main func
def nodeNum(root: TreeNode) -> int:
    if not root:
        return 0
    tree_depth = mostLeftLevel(root, 1)
    return bs(root, 1, tree_depth)

# recursive
def bs(node: TreeNode, level: int, h: int) -> int:
    """
    @param
    level: node在第level层
    h: 整个tree的深度，永远不变，是全局变量
    """
    # Exit condition
    if level == h:
        # 到达最深的一层，返回node自己的个数，也就是1
        return 1

    # 递归主体
    if mostLeftLevel(node.right, level+1) == h:
        # node的右子树的最大深度达到了整个树的最大深度，说明左树是满的
        return 2**(h-level) - 1 + 1 + bs(node.right, level+1, h)
    else:
        # node的右子树的最大深度没有达到整个树的最大深度，说明右树是满的
        return 2**(h-level-1) - 1 + 1 + bs(node.left, level+1, h)


# helper func
def mostLeftLevel(root: TreeNode, startLevel) -> int:
    """
    计算一颗完全二叉树的深度
    """
    level = startLevel
    while root:
        root = root.left
        level += 1
    return level - 1


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print(nodeNum(root))  # True