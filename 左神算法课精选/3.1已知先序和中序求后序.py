__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


from typing import List, Dict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


###############################################
# 给二叉树的先序和中序遍历数组，求后序遍历数组。保证树中没有重复的节点。
###############################################
def getPostOrder(preArr: List[int], inArr: List[int]) -> List[int]:
    if not preArr or not inArr:
        return []

    N = len(preArr)
    postArr = [None] * N
    setPost(preArr, inArr, postArr, 0, N-1, 0, N-1, 0, N-1)
    return postArr


def setPost(preArr, inArr, postArr, L1, R1, L2, R2, L3, R3):
    # 退出条件
    if L1 > R1:  # 越界
        return
    if L1 == R1:  # 只剩下一个数，直接填写
        postArr[L3] = preArr[L1]
        return

    # 填写根节点
    postArr[R3] = preArr[L1]
    # 找到前序的头一个数字(root)在中序里面的位置
    index = inArr.index(preArr[L1])

    # 递归寻找下一个范围内的数字
    # 左子树(a)部分
    setPost(preArr, inArr, postArr, L1+1, index-L2+L1, L2, index-1, L3, index-L2+L3-1)
    # 右子树(b)部分
    setPost(preArr, inArr, postArr, index-L2+L1+1, R1, index+1, R2, index-L2+L3, R3-1)


if __name__ == "__main__":
    preArr = [1, 2, 4, 5, 3, 6, 7]
    inArr = [4, 2, 5, 1, 6, 3, 7]
    postArr = getPostOrder(preArr, inArr)
    print(postArr)