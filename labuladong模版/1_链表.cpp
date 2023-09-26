struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/**
 * 链表反转 (递归写法)
 * 递归思想：什么时候使用递归？子问题 和 原问题 的结构完全相同
 */
ListNode* reverseList1(ListNode* head) {
    // Exit: 如果已经递归到最后一个node了，它的反转就是它自己
    if (head == nullptr || head->next == nullptr) {
        return head;
    }
    // Main
    // 递归的主要意图：把当前节点之后的链表反转好，并返回新的head(也就是原来的last)
    ListNode *last = reverseList(head->next);
    // 此时只需要反转 head 和 head->next，将head和反转好的链表拼起来就好了
    // 当前head的下一个节点 的next 指向head (反转)
    head->next->next = head;
    head->next = nullptr;

    // Return
    // last is the new head
    return last;
}

/**
* 链表反转 (循环写法)
*/
ListNode* reverseList2(ListNode* head) {
    if (head == nullptr) return nullptr;

    ListNode *p1 = head, *p2 = head->next;
    head->next = nullptr;
    while (p2 != nullptr) {
        ListNode *tmp = p1;
        p1 = p2;
        p2 = p2->next;
        p1->next = tmp;

    }
    return p1;
}

/**
 * 反转前N个节点
 */
ListNode *successor = nullptr; //后驱节点

ListNode* reverseN(ListNode* head, int n) {
    // Exit
    if (n == 1) {
        // 记录第 n+1 个节点
        successor = head->next;
        return head;
    }

    // Main
    ListNode *last = reverseList(head->next, n-1);

    head->next->next = head;
    // 让反转之后的 head 和后面的节点连起来
    head->next = successor;

    // Return
    return last;
}

/**
 * 反转链表的一部分
 * 给定索引区间 [m, n] (索引从1开始)，仅反转区间中的链表元素
 */
ListNode* reverseBetween(ListNode* head, int m, int n) {
    // base case
    if (m == 1) {
        return reverseN(head, n);
    }

    // Main: 前进到反转的起点出发 base case
    head->next = reverseBetween(head->next, m-1, n-1);
    return head;
}

/**
 * 反转链表的一部分 (循环写法)
 * 此时给定的直接是两个node (左闭右开)
 */
ListNode* reverseBetween(ListNode* head, int a, int b) {
    ListNode *pre, *cur, *nxt;
    pre = nullptr, cur = a, nxt = b;
    while (cur != b) {
        nxt = cur->next;
        cur->next = pre;
        pre = cur;
        cur = nxt;
    }
    return pre; // 返回反转后的头节点
}

// ---------------------------------------------------------

/**
 * leetcode 25.
 * K个一组翻转链表，最后不足k的部分保持不变
 */
ListNode* reverseBetween(ListNode* head, int k) {
    // base case 1
    if (head == nullptr) return nullptr;

    // 前期准备：区间[a, b) 包含k个待反转元素
    ListNode *a, *b;
    a = b = head;
    for (int i = 0; i < k; i++) {
        // 不足k个的，不需要反转, base case 2
        if (b == nullptr) return head;
        // b-node往前走k次，此时a和b分别指向k个一组的首节点 和 尾节点->next
        b = b->next;
    }

    // 循环法 反转前k个元素
    ListNode *newHead = reverseBetween(a, b);

    // 递归反转后续链表并连接起来
    a->next = reverseKGroup(b, k);

    return newHead;
}


/**
 * leetcode 234.
 * 回文链表
 */

class Solution {
private:
    ListNode* left;
public:
    bool isPalindrome(ListNode* head) {
        this->left = head;
        return traverse(head);
    }

    bool traverse(ListNode* right) {
        // Base
        if (right == nullptr) return true;

        // Main
        bool res = traverse(right->next);
        res = res && (this->left->val == right->val);
        this->left = this->left->next;
        // Return
        return res;
    }
};
