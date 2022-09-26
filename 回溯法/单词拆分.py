"""
@Date:        2022/9/26 上午10:52
@Author:      wyj
@FileName:    单词拆分.py
@Description: None
"""
from typing import List


# def backtrack(s, res, word_dict):
#     for i in range(0, len(s)):
#         print(i, end=" *\n")
#         for j in word_dict:
#             k = len(j)
#             if i + k > len(s):
#                 break
#             if s[:i + k] == j:
#                 print(j, end=" **\n")
#                 res = res + j
#                 print(res, end=' ***\n')
#                 if res == s:
#                     print("*******************")
#                     return True
#                 backtrack(s[:i+k], res, word_dict)
#     return False


def word_break(s: str, word_dict: List[str]) -> bool:
    import functools

    # lru_cache会将函数的输入和输出进行缓存，如果再下次调用此函数时，出现了相同的输入，
    # 那么相同的输出就可直接从缓存中提取，函数体本身无需再次执行
    @functools.lru_cache(None)
    def back_track(s):
        if not s:
            return True
        res = False
        for i in range(1, len(s) + 1):
            if s[:i] in word_dict:
                res = back_track(s[i:]) or res
        return res

    return back_track(s)


if __name__ == "__main__":
    res = word_break(s="leetcode", word_dict=["leet", "code"])
    print(res)
    res = word_break(s="applepenapple", word_dict=["apple", "pen"])
    print(res)
    res = word_break(s="catsandog", word_dict=["cats", "dog", "sand", "and", "cat"])
    print(res)
