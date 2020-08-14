# source: https://www.cnblogs.com/jiaxin359/p/9265208.html


class UnionFindSet(object):
    def __init__(self, data_list):
        """
        初始化两个字典，一个保存父节点，一个保存父节点的大小。
        初始化时，将父节点设为自身，size设为1

        :param data_list: 输入数据
        """
        self.parent = dict()
        self.size_map = dict()

        for node in data_list:
            # 刚开始时，每个node都是一个独立的集合
            self.parent[node] = node
            self.size_map[node] = 1

    def find_head(self, node):
        """
        使用递归方式查找父节点，
        在查找父节点的同时，顺便把当前节点移动到父节点上去。

        :param node:
        :return:
        """
        if node == self.parent[node]:
            # node自己的父节点就是node本身，说明已经找到了父节点
            # 返回父节点到递归的上一级函数
            return node
        # 不满足if条件，则node上面还有父节点，继续往上找
        # 当find返回时，返回的是最顶部的父节点，此时这个赋值语句还起到了把当前query的节点直接接到父节点上的作用
        self.parent[node] = self.find_head(self.parent[node])
        # 返回父节点
        return self.parent[node]

    def is_same_set(self, node_a, node_b):
        """
        检查两个node是否在同一个集合里面
        """
        return self.find_head(node_a) == self.find_head(node_b)

    def union(self, node_a, node_b):
        """
        将两个集合合并在一起
        :param index1:
        :param index2:
        :return:
        """
        if node_a is None or node_b is None:
            return

        # 找到各自集合的代表节点
        a_head = self.find_head(node_a)
        b_head = self.find_head(node_b)

        if a_head != b_head:
            a_set_size = self.size_map[a_head]
            b_set_size = self.size_map[b_head]
            # 比较两个集合的大小，小集合并到大集合下面去
            if a_set_size >= b_set_size:
                self.parent[b_head] = a_head
                self.size_map[a_head] = a_set_size + b_set_size
                del self.size_map[b_head]
            else:
                self.parent[a_head] = b_head
                self.size_map[b_head] = a_set_size + b_set_size
                del self.size_map[a_head]

    def max_size(self):
        """
        返回所有集合中包含元素最多的元素个数
        """
        ans = 0
        for s in self.size_map.values():
            ans = max(ans, s)
        return ans

    def num_sets(self):
        """
        返回一共有多少个集合
        """
        return len(self.size_map.keys())
            


