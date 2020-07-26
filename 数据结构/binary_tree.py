"""binary_tree.py"""
__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


from typing import List, Dict
import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#####################################
# 读取牛客网的输入 构建二叉树
#
# 输入描述：
# 第一行输入两个整数 n 和 root，n 表示二叉树的总节点个数，root 表示二叉树的根节点。
# 以下 n 行每行三个整数 fa，lch，rch，表示 fa 的左儿子为 lch，右儿子为 rch。(如果 lch 为 0 则表示 fa 没有左儿子，rch同理)

# 示例：
# 3 2
# 1 2 3
# 2 4 5
# 4 0 6
# 5 0 0
# 3 0 0
# 表示：
#      1
#    2   3
#  4  5
#   6
#####################################
# 递归读取输入
def build_tree(node, count):
    if not node:
        return

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    root, L, R = list(map(int, line.split()))

    if L != 0:
        node.left = TreeNode(L)
        build_tree(node.left, count-1)
    if R != 0:
        node.right = TreeNode(R)
        build_tree(node.right, count-1)
# main
line = sys.stdin.readline().strip()
n, root_val = list(map(int, line.split()))
root = TreeNode(root_val)
build_tree(root, n)
# further processing
# =======================================

# 先存在列表里，再读取输入
# 用left_queue存储每次的左节点
# 用right_stack存储每次的右节点
def build_tree2(root_val, count):
    all_values = [root_val]
    for _ in range(count):
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        all_values += values[1:]

    val = all_values.pop(0)
    root = TreeNode(val)
    left_queue = [root]
    right_stack = list()
    while left_queue + right_stack:
        if left_queue:
            node = left_queue.pop(0)  # pop第一个
        else:
            node = right_stack.pop()  # pop最后一个

        left = all_values.pop(0)
        right = all_values.pop(0)
        if left != 0:
            node.left = TreeNode(left)
            left_queue.append(node.left)
        if right != 0:
            node.right = TreeNode(right)
            right_stack.append(node.right)

    return root
# main
line = sys.stdin.readline().strip()
n, root_val = list(map(int, line.split()))
build_tree(root_val, n)
# further processing
# ================================================
# ================================================


#####################################
# 读取LeetCode的输入 构建二叉树
#               5
#             /   \
#            4     8
#           /     / \
#          11    13  4
#         /  \      / \
#        7    2    5   1
#####################################
def build_tree_leetcode(arr: List) -> TreeNode:
    if not arr:
        return

    val = arr.pop(0)
    root = TreeNode(val)
    queue = [root]
    while queue and arr:
        node = queue.pop(0)
        left = arr.pop(0)
        right = arr.pop(0)

        if left:
            node.left = TreeNode(left)
            queue.append(node.left)
        if right:
            node.right = TreeNode(right)
            queue.append(node.right)

    return root

# main
arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
root = build_tree_leetcode(arr)
# ================================================
# ================================================

#####################################
# 打印二叉树（横向看）
#####################################
def print_tree(root: TreeNode, num_nodes: int):
    """
    num_nodes: 树中的节点数（不包括None）
    """
    print("Binary Tree")
    print_inOrder(root, 0, "H", num_nodes)
    print()


def print_inOrder(root: TreeNode, height: int, to: str, length: int):
    if not root:
        return
    print_inOrder(root.right, height + 1, "v", length)
    val: str = to + str(root.val) + to
    lenM = len(val)
    lenL = (length - lenM) // 2
    lenR = length - lenM - lenL
    val = get_space(lenL) + val + get_space(lenR)
    print(get_space(height * length) + val)
    print_inOrder(root.left, height + 1, "^", length)


def get_space(num: int) -> str:
    space = ' '
    buf = list()
    for i in range(num // 2):
        buf.append(space)
    return "".join(buf)
# ================================================
# ================================================

if __name__ == "__main__":
    pass

# 测试用例
"""
42 1
1 17 19
17 31 35
31 0 0
35 20 38
20 18 28
18 0 0
28 0 0
38 3 6
3 7 10
7 0 16
16 30 42
30 0 41
41 0 0
42 0 0
10 0 0
6 40 5
40 21 8
21 4 0
4 0 0
8 0 0
5 0 29
29 25 27
25 0 26
26 0 0
27 0 0
19 39 32
39 33 0
33 22 13
22 36 11
36 0 9
9 0 0
11 0 0
13 12 0
12 0 0
32 23 15
23 14 37
14 2 34
2 0 0
34 0 0
37 24 0
24 0 0
15 0 0
"""