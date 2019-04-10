# 题目：
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：
#   输入: "babad"
#   输出: "bab"
# 注意: "aba" 也是一个有效答案。

# 示例 2：
#   输入: "cbbd"
#   输出: "bb"

# Solution Code1
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if (s == ''):
            return s
        ss = s[::-1]
        s_len = len(s)
        res_len = 1
        res_str = s[0]
        for i in xrange(s_len):
            for j in xrange(i+res_len+1,s_len+1):
                if (s[i:j] == ss[s_len-j:s_len-i]):
                    res_len = j-i
                    res_str = s[i:j]
        return res_str
        
 # Solution Code2: 动态规划dp
 class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.longestPalindromecore(s)
    def longestPalindromecore(self, s):
        if len(s)<=1:
            return s
        if len(s)==2:
            if s[0]==s[1]:
                return s
            else:
                return s[1]#或者s[0]?
        max_s = self.longestPalindromecore(s[:-1])
        if len(max_s)==1:
            if s[-1]==s[-3]:
                return s[-3:]
            elif s[-2]==s[-1]:
                return s[-2:]
            else:
                return s[-1]   
        if self.judge_palindrome(s[-len(max_s)-2:]):
            return s[-len(max_s)-2:]
        elif self.judge_palindrome(s[-len(max_s)-1:]):
            return s[-len(max_s)-1:]
        else:
            return max_s
    def judge_palindrome(self, sub_s):
        if len(sub_s)==1:
            return True
        for i in range(len(sub_s)//2):
            if sub_s[i]!=sub_s[-i-1]:
                return False
        return True
        
 # Soltion Code3:
# 第一种思路:
# 以每个字母为回文中心,考虑回文长度为奇数和偶数的情况.

# 第二种思路:
# 以每个字母为回文串的结束标志,分别考虑可能回文为奇数和偶数的情况.

# 第三种思路:
# 令dp[j][i]从字符串j到i是否为回文串
# 动态回归方程 dp[j][i]是看j+1和i-1是否为回文串.

# 第一种思路
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.start = 0
        self.max_len = 0
        n = len(s)
        if n < 2:
            return s

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            if self.max_len < j - i - 1:
                # print(i,j)
                self.max_len = j - i - 1
                self.start = i + 1

        for k in range(n):
            #print(k)
            helper(k, k)
            helper(k, k + 1)
        return s[self.start:self.start + self.max_len ]

# 第二种思路   （耗时最优48ms）
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2 or s == s[::-1]:
            return s
        max_len = 1
        start = 0
        for i in range(1,n):
            even = s[i-max_len:i+1]
            odd = s[i-max_len-1:i+1]
            if i-max_len-1>=0 and odd == odd[::-1]:
                start = i-max_len-1
                max_len += 2
                continue
            if i-max_len>=0 and even == even[::-1]:
                start = i-max_len
                max_len += 1
        return s[start:start+max_len]

# 第三种思路
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = float("-inf")
        res = ""
        for i in range(n):
            # dp[i][i] = 1
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j < 2 or dp[i - 1][j + 1]):
                    dp[i][j] = 1

                if dp[i][j] and i - j + 1 > max_len:
                    max_len = i - j + 1
                    res = s[j:i + 1]
        # print(dp)
        return res
