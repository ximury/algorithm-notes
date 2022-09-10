"""
@Date:        2022/9/10 下午2:20
@Author:      wyj
@FileName:    find_from_matrix.py
@Description: None
"""
from typing import List


# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 20
def perfect(matrix: List[list], target):
    """Z字形查找
    时间复杂度：O(m + n)
    在搜索的过程中，如果我们没有找到 target，那么我们要么将 y 减少 1，要么将 x 增加 1。
    由于(x,y) 的初始值分别为 (0, n-1)
    因此 y 最多能被减少 n 次，x 最多能被增加 m 次，总搜索次数为 m + n
    在这之后，x 和 y 就会超出矩阵的边界。
    空间复杂度：O(1)

    :param matrix:
    :param target:
    :return:
    """
    col = 0
    row = len(matrix) - 1
    # while True:
    while row >= 0 and col < len(matrix[0]):
        if target > matrix[row][col]:
            # col = col + 1
            col += 1
        elif target < matrix[row][col]:
            row -= 1
            # row = row - 1
        else:
            return True
        # if row < 0 or col >= len(matrix[0]):
        #     return False
    return False


def best_search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    时间复杂度：O(m log n)
    对一行使用二分查找的时间复杂度为 O(log n)，最多需要进行 m 次二分查找。
    空间复杂度：O(1)

    :param matrix:
    :param target:
    :return:
    """
    import bisect

    for row in matrix:
        idx = bisect.bisect_left(row, target)
        if idx < len(row) and row[idx] == target:
            return True
    return False


if __name__ == "__main__":
    matrix_param = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    res = perfect(matrix_param, target=17)
    print(res)
    res = best_search_matrix(matrix_param, target=20)
    print(res)
