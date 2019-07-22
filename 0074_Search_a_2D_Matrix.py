# 搜索二维矩阵
# 题目:
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。

# 示例 1:
#   输入:
#   matrix = [
#     [1,   3,  5,  7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 50]
#   ]
#   target = 3
#   输出: true

# 示例 2:
# 输入:
#   matrix = [
#     [1,   3,  5,  7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 50]
#   ]
#   target = 13
#   输出: false

# Solution Code
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        r, c = len(matrix), len(matrix[0])
        left, right = 0, r * c

        while left < right:
            mid = (left + right) // 2
            m, n = mid // c, mid % c
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] < target:
                left = mid + 1
            else:
                right = mid

        return False


if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13
    print(Solution().searchMatrix(matrix, target))
