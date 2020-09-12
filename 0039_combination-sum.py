# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-9-9 22:14
# software: PyCharm
"""
题目：组合总和

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 回溯
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        dfs(candidates, 0, size, path, res, target)
        return res


# 回溯 + 剪枝
class Solution1(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        size = len(candidates)
        candidates.sort()

        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path)
                return

            for i in range(begin, size):
                rest = target - candidates[i]
                if rest < 0:
                    break
                dfs(candidates, i, size, path + [candidates[i]], res, rest)

        if size == 0:
            return []
        dfs(candidates, 0, size, path, res, target)

        return res


if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8
    solution = Solution()
    res = solution.combinationSum(candidates, target)
    print(res)

    solution1 = Solution1()
    res1 = solution1.combinationSum(candidates, target)
    print(res1)
