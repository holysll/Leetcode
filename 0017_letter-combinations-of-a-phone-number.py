# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-26 22:26
# software: PyCharm
"""
题目：电话号码的字母组合

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import itertools


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        l_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        chars = [l_map.get(d) for d in digits]
        return [''.join(x) for x in itertools.product(*chars)]


class Solution1(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits:
            return []

        res = []

        def dfs(tmp, index):
            if (index == len(digits)):
                res.append(tmp)
                return
            num = digits[index]
            chars = d[num]

            for i in chars:
                dfs(tmp + i, index + 1)

        dfs("", 0)
        return res


class Solution3(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        temp = ['']
        ans = []
        for d in digits:
            ans = []
            for char in temp:
                for new_char in mapping[d]:
                    ans.append(char + new_char)
            temp = ans
        return ans


if __name__ == '__main__':
    digits = "27"
    solution = Solution()
    res = solution.letterCombinations(digits)
    print(res)

    solution1 = Solution1()
    res1 = solution1.letterCombinations(digits)
    print(res1)

    solution1 = Solution1()
    res1 = solution1.letterCombinations(digits)
    print(res1)
