__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


class Trie:
    def __init__(self):
        self.root = dict()
        self.end = -1

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_node = self.root  # self.root 会随着curr_node的改变而改变
        # 遍历word中每一个字符
        for ch in word:
            # 如果字符不在curr_node的key里面则单独开一个dict，说明接下来的字符都是新的连接，新开一个分支
            if ch not in curr_node.keys():
                curr_node[ch] = dict()
            # 继续往下遍历，如果是新开的分支，那么curr_node为空字典
            curr_node = curr_node[ch]
        curr_node[self.end] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr_node = self.root
        for ch in word:
            if ch not in curr_node:
                return False
            curr_node = curr_node[ch]

        # if it doesn't end here
        if self.end not in curr_node:
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr_node = self.root
        for c in prefix:
            if c not in curr_node:
                return False
            curr_node = curr_node[c]

        return True
