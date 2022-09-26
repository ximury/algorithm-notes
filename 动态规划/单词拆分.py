"""
@Date:        2022/9/26 上午11:25
@Author:      wyj
@FileName:    单词拆分.py
@Description: None
"""
from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    # dp[i] 表示 s 的前 i 位是否可以用 word_dict 中的单词表示
    dp = [False] * (len(s) + 1)
    print(f"origin: {dp}")
    dp[0] = True
    for i in range(1, len(s) + 1):
        for x in word_dict:
            # if i >= len(x):
            #     print(i - len(x), s[i - len(x):i])
            if i >= len(x) and s[i - len(x) : i] == x and dp[i - len(x)]:
                dp[i] = True
                break
    print(f"updated: {dp}")
    return dp[-1]


def word_break2(s: str, word_dict: List[str]) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(n):
        for j in range(i + 1, n + 1):
            if dp[i] and (s[i:j] in word_dict):
                dp[j] = True
    print(f"updated: {dp}")
    return dp[-1]


def word_break3(s: str, word_dict: List[str]) -> bool:
    # 动态规划优化（只记录True值）
    trues = [0]
    for j in range(0, len(s) + 1):
        for i in trues:
            if s[i:j] in word_dict:
                trues.append(j)
                break
    print(f"updated: {trues}")
    return trues[-1] == len(s)


if __name__ == "__main__":
    word_break(s="leetcode", word_dict=["leet", "code"])
    word_break2(s="applepenapple", word_dict=["apple", "pen"])
    word_break3(s="catsandog", word_dict=["cats", "dog", "sand", "and", "cat"])
