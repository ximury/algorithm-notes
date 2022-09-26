"""
@Date:        2022/9/26 上午10:15
@Author:      wyj
@FileName:    字符串分割回文串.py
@Description: None
"""


# 通用模板

# res = []
# path = []
#
# def backtrack(未探索区域, res, path):
#     if 未探索区域满足结束条件:
#         res.add(path) # 深度拷贝
#         return
#     for 选择 in 未探索区域当前可能的选择:
#         if 当前选择符合要求:
#             path.add(当前选择)
#             backtrack(新的未探索区域, res, path)
#             path.pop()


def is_palindrome(st):
    return st == st[::-1]


def backtrack(s, res, path):
    if not s:
        res.append(path)
        return
    for i in range(1, len(s) + 1):
        if is_palindrome(s[:i]):
            print(path, s[:i], path + [s[:i]])
            backtrack(s[i:], res, path + [s[:i]])


def partition(s):
    res = []
    backtrack(s, res, [])
    print(res)
    return res


def range_test():
    num = "asd"
    for i in range(1, len(num) + 1):
        print(i, num[:i])
    print(num, num[:])
    print(num[0:], num[1:])
    print(num[:2])
    print("------------------")

if __name__ == "__main__":
    range_test()
    partition("aaba")
