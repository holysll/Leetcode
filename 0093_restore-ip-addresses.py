# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-9 20:10
# software: PyCharm
"""
题目：复原IP地址

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        num = 4
        ans = []

        def dfs(start, path):

            # 结束条件
            if len(path) > num or (len(path) == num and start < len(s) - 1):
                return
            # 追加结果
            if start >= len(s):
                if len(path) == num:
                    ans.append('.'.join(path))
                return
            # 当前是0 ，特殊情况处理
            if s[start] == '0':
                path.append(s[start])
                dfs(start + 1, path)
                path.pop()
                return

            # 递归查找
            for i in range(start, len(s)):
                if 0 <= int(s[start:i + 1]) <= 255:
                    path.append(s[start:i + 1])
                    dfs(i + 1, path)
                    path.pop()
                else:
                    break
            return

        dfs(0, [])
        return ans


class Solution1(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        def backtrack(track, start, s):
            # 满四段且用光所有字符串
            if len(track) == 4 and start == len(s):
                res.append('.'.join(track))
            # 满四段但没用光所有字符串
            if len(track) == 4 and start < len(s):
                return

            for j in range(1, 4):
                # 字符不存在，超出边界，最后一个字符的索引为s[start + j - 1]
                if (start + j - 1) >= len(s):
                    return
                # 若选择长度超过2的字符串，则不能是‘0’开头
                if j >= 2 and s[start] == "0":
                    return
                tmp = s[start: start + j]
                # 长度为3的字符串，取值不能大于255
                if j == 3 and int(tmp) > 255:
                    return
                backtrack(track + [tmp], start + j, s)
        backtrack([], 0, s)
        return res

if __name__ == '__main__':
    s = "25525511135"
    solution = Solution()
    res = solution.restoreIpAddresses(s)
    print(res)

    solution1 = Solution1()
    res1 = solution1.restoreIpAddresses(s)
    print(res1)
