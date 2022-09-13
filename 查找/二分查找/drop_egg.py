"""
@Date:        2022/9/13 上午10:16
@Author:      wyj
@FileName:    drop_egg.py
@Description: https://leetcode.cn/leetbook/read/top-interview-questions/xmup75/
"""


def super_egg_drop(kk: int, nn: int) -> int:
    """动态规划 + 二分查找

    时间复杂度：O(kn log n)，需要计算 O(kn) 个状态，每个状态计算时需要 O(log n) 的时间进行二分查找；

    空间复杂度：O(kn)，需要 O(kn) 的空间存储每个状态的解

    :param kk: 剩余鸡蛋数
    :param nn: 楼层数
    :return:
    """
    # 状态表示（k, n-x）
    # x: 从x层仍鸡蛋，如果不碎，状态更新为（k, x至n）
    # 如果碎了，状态更新为（k-1, 0至x-1）
    # 1≤x≤n
    # dp(k,n)=1+ min(max(dp(k−1,x−1),dp(k,n−x)))
    memo = {}

    def dp(k, n):
        print(k, n, end="**\n")
        if (k, n) not in memo:
            if n == 0:
                ans = 0
            elif k == 1:
                ans = n
            else:
                # 最低1层，最高n层
                low, high = 1, n
                while low + 1 < high:
                    x = (low + high) // 2
                    print("计算t1", end=":\n")
                    t1 = dp(k - 1, x - 1)
                    print("计算t2", end=":\n")
                    t2 = dp(k, n - x)
                    if t1 < t2:
                        low = x
                    elif t1 < t2:
                        high = x
                    else:
                        low = high = x
                ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x)) for x in (low, high))
            memo[k, n] = ans
            print(f"memo[{k} {n}] = {memo[k, n]}", end="&\n")
        print(memo, end="&&\n")
        return memo[k, n]

    print("$$$")
    return dp(kk, nn)


def super_egg_drop2(k: int, n: int) -> int:
    """决策单调性

    时间复杂度：O(kn)，需要计算 O(kn) 个状态，
    同时对于每个 k，最优解指针只会从 0 到 n 走一次，复杂度也是 O(kn)，因此总体复杂度为 O(kn)；

    空间复杂度：O(n)。因为 dp 每一层的解只依赖于上一层的解，因此每次只保留一层的解，需要的空间复杂度为 O(n)。

    :param k:
    :param n:
    :return:
    """
    dp = list(range(n + 1))
    dp2 = [0] * (n + 1)
    for k in range(2, k + 1):
        x = 1
        for m in range(1, n + 1):
            while x < m and max(dp[x - 1], dp2[m - x]) >= max(dp[x], dp2[m - x - 1]):
                x += 1
            dp2[m] = 1 + max(dp[x - 1], dp2[m - x])

        dp = dp2[:]

    return dp[-1]


if __name__ == "__main__":
    # 已知存在楼层 f ，满足 0 <= f <= n ，
    # 任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破
    # 计算并返回要确定 f 确切的值 的 最小操作次数 是多少
    res = super_egg_drop(kk=1, nn=2)
    print(f"(1, 2)最小操作次数: {res}")
    res = super_egg_drop(kk=2, nn=6)
    print(f"(2, 6)最小操作次数: {res}")
    res = super_egg_drop2(k=3, n=14)
    print(f"(3, 14)最小操作次数: {res}")
