__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


from typing import List, Dict

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

###############################################
# 测试模块
###############################################
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
##############################################

###############################################
# 给一棵二叉树A，求二叉树B是否为A的子树。
# (注意！这个和剑指offer26的"树的子结构"不一样。
# "子树"必须是某节点开始下面的所有节点；
# "子结构"可以是下面的部分节点，只要结构一样就行)

# 思路：
# 把A、B都序列化成字符串，然后相当于比较一个字符串是否包含
# 另一个字符串
###############################################
def isSubTree(t1: TreeNode, t2: TreeNode) -> bool:
    # 把树用前序遍历的方式转化为列表
    arr1 = list()
    arr2 = list()
    serializeTree2Arr(t1, arr1)
    serializeTree2Arr(t2, arr2)
    # 比较是否有字符串包含
    str1 = "".join(arr1)
    str2 = "".join(arr2)
    return str1.find(str2) != -1


def serializeTree2Arr(root: TreeNode, arr: List[str]):
    if not root:
        arr.append('#')
    else:
        arr.append(str(root.val))
        serializeTree2Arr(root.left, arr)
        serializeTree2Arr(root.right, arr)

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, None, 8, 9, None, None, None, None, None]
    arr2 = [2, 4, 5, None, 8, 9, None]
    t1 = build_tree_leetcode(arr1)
    t2 = build_tree_leetcode(arr2)

    print(isSubTree(t1, t2))  # True
