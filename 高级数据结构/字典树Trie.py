"""common.py: common tools"""
__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"

import glob
import os
import tqdm

class Trie:
    def __init__(self):
        self.root = dict()
        self.end = -1

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_node = self.root  # self.root 会随着curr_node的改变而改变
        for ch in word:
            if ch not in curr_node:
                curr_node[ch] = dict()
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
	

