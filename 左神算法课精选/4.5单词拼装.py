__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"

import tqdm
from typing import List, Dict

#####################################################
# 假设所有字符都是小写字母，大字符串string，arr是去重的单词表
# 每个单词都不是空字符串且可以使用任意次。
# 使用arr中的单词有多少中拼接成string的方式
# 返回方法数

# 例：
# string = "aaaab"
# arr = ["a", "aa", "b"]
# 1) a + a + a + a + b
# 2) a + a + aa + b
# 3) a + aa + a + b
# 4) aa + aa + b
# 5) aa + a + a + b
#####################################################


# ===================================================
# 递归方法
# ===================================================
def word_ensemble1(string: str, words: List[str]) -> int:
    return recursive(string, 0, words)


def word_ensemble2(string: str, words: List[str]) -> int:
    return recursive2(string, 0, words)


def recursive(string: str, index: int, words: List[str]) -> int:
    """
    每次递归只需要考虑 string 中从index开始的substring能提供几种方案
    """
    # Exit condition
    if index == len(string):  # 递归到了string末尾，返回1种方法
        return 1

    # Main body
    ways = 0
    # 遍历给定的string，看从index～e这个子串，是否在words中
    for e in range(index, len(string)):
        if string[index:e+1] in words:
            ways += recursive(string, e+1, words)

    return ways


def recursive2(string: str, index: int, words: List[str]) -> int:
    # Exit condition
    if index == len(string):
        return 1

    # Main body
    ways = 0
    # 遍历给的单词，然后比对字符串中从index ~ len(words[i]) 有没有能对应上当前word的。
    for i in range(len(words)):
        l = len(words[i])
        if words[i] == string[index:index+l]:
            ways += recursive(string, index+l, words)

    return ways
# ===================================================
# ===================================================

# ===================================================
# 动态规划

# 从上面第一个递归函数可以看出：
# 退出条件是 dp[N] = 1，然后再慢慢往回推导
# 也就是说dp[i] 应该是会依赖后面 i+1 ～ N 的所有位置
# ===================================================
def word_ensemble3(string: str, words: List[str]) -> int:
    words_set = set(words)
    N = len(string)

    dp = [0] * (N + 1)
    dp[N] = 1

    for i in reversed(range(N)):  # i 反向遍历字符串，从 N-1 遍历到 0
        for j in range(i, N):     # j 从i开始，往后遍历
            if string[i:j+1] in words:
                # 取substring，如果substring是属于words里给定的一个单词，则加上
                dp[i] += dp[j+1]

    return dp[0]

# ===================================================
# 进一步优化：
# if string[i:j+1] in words
# 这个查询过程，可以用字典树来进行优化
# ===================================================

class TrieNode:
    def __init__(self):
        self.nexts = dict()
        self.end = False


def word_ensemble4(string: str, words: List[str]) -> int:

    trie = init_trie(words)

    # DP
    words_set = set(words)
    N = len(string)

    dp = [0] * (N + 1)
    dp[N] = 1

    for i in reversed(range(N)):  # i 反向遍历字符串，从 N-1 遍历到 0
        # 每次遍历到string的一个新的位置，都从头开始找字典树
        cur = trie
        for j in range(i, N):  # j 从i开始，往后遍历
            # 用以下字典树的查询代替： if string[i:j + 1] in words:
            if string[j] not in cur.nexts.keys():
                # 如果遍历到字典树某个地方根本找不到当前字符，直接break，后面的字符必然也不在字典树中
                break
            cur = cur.nexts[string[j]]
            if cur.end:
                dp[i] += dp[j + 1]

    return dp[0]


def init_trie(words: List[str]):
    root = TrieNode()
    for w in words:
        node = root
        for char in w:
            if char not in node.nexts.keys():
                node.nexts[char] = TrieNode()
            node = node.nexts[char]
        node.end = True

    return root
# ===================================================
# ===================================================


#####################################################
# 随机样本生成器
#####################################################
import random
class RandomSample:
    def __init__(self, s: str, w: List[str]):
        self.string = s
        self.words = w

    def print_info(self):
        print(self.string)
        print(self.words)


def generate_random_sample(candidates: List[str], max_arr_len: int, max_str_len: int, joint: int):
    word_book = random_seeds(candidates, max_arr_len, max_str_len)
    # get rid of duplicated words in word_book
    test_set = set(word_book)
    word_book = list(test_set)

    all = list()
    for i in range(joint):
        elem = word_book[random.randint(0, len(word_book)-1)]
        all.append(elem)

    return RandomSample("".join(all), word_book)


def random_seeds(candidates: List[str], max_arr_len: int, max_str_len: int):
    """
    随机生成题目中的 words 数组
    """
    # init arr，大小是1 ~ max_arr_len
    word_book = list()
    arr_len = random.randint(1, max_arr_len)
    for i in range(arr_len):
        string = ''
        str_len = random.randint(1, max_str_len)
        for j in range(str_len):
            string += candidates[random.randint(0, len(candidates)-1)]
        word_book.append(string)

    return word_book
#####################################################
# END of 随机样本生成器
#####################################################

if __name__ == "__main__":

    # print(word_ensemble4("aaaab", ["a", "aa", "b"]))

    candidates = ['a', 'b']
    max_arr_len = 20
    max_str_len = 4
    joint = 5
    num_tests = 3000
    test_result = True
    for i in tqdm.tqdm(range(num_tests)):
        sample = generate_random_sample(candidates, max_arr_len, max_str_len, joint)
        ans1 = word_ensemble1(sample.string, sample.words)
        ans2 = word_ensemble2(sample.string, sample.words)
        ans3 = word_ensemble3(sample.string, sample.words)
        ans4 = word_ensemble4(sample.string, sample.words)
        if ans1 == ans2 == ans3 == ans4:
            continue
        else:
            test_result = False
            print("The following test case failed")
            sample.print_info()
            print("ans1=" + str(ans1), "ans2=" + str(ans2), "ans3=" + str(ans3), "ans4=" + str(ans4))
            break

    print(str(num_tests) + "次随机测试是否通过：" + str(test_result))
