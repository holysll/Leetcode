# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-6 15:32
# software: PyCharm
"""
题目：回文对

给定一组互不相同的单词，找出所有不同的索引对(i, j)，使得列表中的两个单词，words[i] + words[j]，可拼接成回文串。

示例 1：
输入：["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]]
解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]

示例 2：
输入：["bat","tab","cat"]
输出：[[0,1],[1,0]]
解释：可拼接成的回文串为 ["battab","tabbat"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 自己写的，超时
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        nums = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    nums.append([i, j])
        res = []
        for item in nums:
            s = words[item[0]] + words[item[1]]
            if s == s[::-1]:
                res.append(item)

        return res

# 优化，超时
class Solution1(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    s = words[i] + words[j]
                    if s == s[::-1]:
                        res.append([i,j])
        return res


# 排列方法，超时
from itertools import permutations
class Solution2(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        nums = [i for i in range(len(words))]
        for item in permutations(nums, 2):
            s = words[item[0]] + words[item[1]]
            if s == s[::-1]:
                res.append(list(item))
        return res

# 前缀和后缀，利用哈希字典
# 核心思想--枚举前缀和后缀
# 如果两个字符串k1，k2组成一个回文字符串会出现三种情况
# len(k1) == len(k2),则需要比较k1 == k2[::-1]
# len(k1) < len(k2),例如，k1=a, k2=abb,可组成abba
#   因为k2后缀bb已经是回文字符串了，则需要找k1与k2剩下相等的部分
# len(k1) > len(k2),例如，k1=bba, k2=a,组成abba
#   因为k1前缀bb已经是回文字符串了，则需要找k1剩下与k2相等的部分
class Solution3(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        word_dict = {word: i for i, word in enumerate(words)}  # 构建一个字典，key为word，value为索引
        for i, word in enumerate(words):
            for j in range(len(word)+1):  # 切片左闭右开，故+1
                tmp1 = word[:j]  # 字符串的前缀
                tmp2 = word[j:]  # 字符串的后缀
                if (tmp1[::-1] in word_dict) and (word_dict[tmp1[::-1]] != i) and (tmp2 == tmp2[::-1]):
                    # 当word的前缀在字典中，且不是word自身，且word剩下的部分也是回文（空也是回文），则说明存在能与word组成回文的字符串
                    res.append([i,word_dict[tmp1[::-1]]])  # 返回此时的word下标和找到字符串的下标

                if j > 0 and (tmp2[::-1] in word_dict) and (word_dict[tmp2[::-1]] != i) and (tmp1 == tmp1[::-1]):
                    # 注意：因为是后缀，所以至少要从word的第二位算起，所以j > 0
                    # 当word的后缀在字典中，且不是word自身，且word剩下的部分是回文（空也是回文），则说明存在能与word组成回文的字符串
                    res.append([word_dict[tmp2[::-1]], i])  # 返回找到的字符串下标和此时word的下标

        return res


if __name__ == '__main__':
    words = ["abcd","dcba","lls","s","sssll"]
    solution = Solution()
    res = solution.palindromePairs(words)
    print(res)

    solution1 = Solution1()
    res1 = solution1.palindromePairs(words)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.palindromePairs(words)
    print(res2)

    solution3 = Solution3()
    res3 = solution3.palindromePairs(words)
    print(res3)
