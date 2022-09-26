"""
@Date:        2022/9/21 上午9:57
@Author:      wyj
@FileName:    字符串反转.py
@Description: None
"""
from functools import reduce


def method1(s: str):
    ss = s[::-1]
    print(ss)


def method2(s: str):
    ss = reduce(lambda x, y: y + x, s)
    print(ss)


def method3(s: str):
    ss = list(s)
    ss.reverse()
    ss = "".join(ss)
    print(ss)


def method4(s: str):
    # 栈
    l0 = list(s)  # 模拟入栈
    ss = ""
    while len(l0) > 0:
        ss.join(l0.pop())
    print(ss)


if __name__ == "__main__":
    s0 = "asdfg"
    method1(s0)
    print(s0, end="----\n")
    method2(s0)
    method3(s0)
    method4(s0)
