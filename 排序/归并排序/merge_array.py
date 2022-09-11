"""
@Date:        2022/9/11 上午9:19
@Author:      wyj
@FileName:    merge_array.py
@Description: None
"""
from typing import List


def merge1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """直接合并后排序
    时间复杂度：O((m+n)log(m+n))，排序序列长度为 m+n，套用快速排序的时间复杂度即可
    空间复杂度：O(log(m+n))，排序序列长度为 m+n，套用快速排序的空间复杂度即可
    :param nums1:
    :param m:
    :param nums2:
    :param n:
    :return:
    """
    nums1[m:] = nums2
    nums1.sort()
    # nums1 = sorted(nums1)
    print(nums1)


def merge2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """双指针
    时间复杂度：O(m+n)，指针移动单调递增，最多移动 m+n 次
    空间复杂度：O(m+n)，需要建立长度为 m+n 的中间数组 sorted
    :param nums1:
    :param m:
    :param nums2:
    :param n:
    :return:
    """
    sorted_nums = []
    p1, p2 = 0, 0
    while p1 < m or p2 < n:
        print(p1, p2, end="--\n")
        if p1 == m:
            # 列表nums1合并完成，直接追加剩余的nums2
            sorted_nums.append(nums2[p2])
            p2 += 1
        elif p2 == n:
            # 列表nums2合并完成，直接追加剩余的nums1
            sorted_nums.append(nums1[p1])
            p1 += 1
        elif nums1[p1] < nums2[p2]:
            sorted_nums.append(nums1[p1])
            p1 += 1
        else:
            sorted_nums.append(nums2[p2])
            p2 += 1
    nums1[:] = sorted_nums
    # nums1 = sorted
    print(nums1)


if __name__ == '__main__':
    """
    合并两个有序数组
    """
    li1 = [1, 2, 3, 0, 0, 0]
    m1 = 3
    li2 = [0, 5, 6]
    n1 = 3
    # merge1(li1, m1, li2, n1)
    print(li1, li2, end="**\n")
    merge2(li1, m1, li2, n1)

# 笔记：
# 1、删除列表前段所有0元素，直至第一个非0元素
# import operator
# from itertools import dropwhile
# li = list(dropwhile(operator.not_, li))

# 2、列表分片操作
# y = x[:]
# 通过分片操作将列表x的元素全部拷贝给y，
# 如果简单的把x赋值给y, 即 y = x，y和x还是指向同一个列表，并没有产生新的副本
