#include <iostream>
#include <unordered_map>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

/**
 * 二叉树的所有问题，就是让你在前中后序位置注入巧妙的代码逻辑，去达到自己的目的，
 * 你只需要单独思考每一个节点应该做什么，其他的不用你管，抛给二叉树遍历框架，
 * 递归会在所有节点上做相同的操作。
 */
void traverse(TreeNode root) {
    if (root == nullptr) return;

    // 前序位置: 刚进入二叉树节点的时候执行
    traverse(root.left)
    // 中序位置: 左子树都遍历完，即将开始遍历右子树的时候执行
    traverse(root.right)
    // 后序位置: 将要离开一个二叉树节点的时候执行
}



