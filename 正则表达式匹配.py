# 题目
# 给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

# '.' 匹配任意单个字符。
# '*' 匹配零个或多个前面的元素。
# 匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

# 说明:
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

# 示例 1:
# 输入:
#   s = "aa"
#   p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。

# 示例 2:
# 输入:
#   s = "aa"
#   p = "a*"
# 输出: true
#   解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。

# 示例 3:
# 输入:
#   s = "ab"
#   p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。

# 示例 4:
# 输入:
#   s = "aab"
#   p = "c*a*b"
# 输出: true
# 解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。

# 示例 5:
# 输入:
#   s = "mississippi"
#   p = "mis*is*p*."
# 输出: false

# Solution Code1 :动态规划
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(len(s)+1)] for j in range(len(p)+1)]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            for j in range(0, len(s)+1):
                if p[i-1] == '.':
                    if i >= 2 and p[i-2] == '*' and j == 0:
                        dp[i][j] = False
                    if j >= 1 and dp[i-1][j-1] is True:
                        dp[i][j] = True
                elif p[i-1] == '*':
                    if dp[i-1][j] is True:
                        dp[i][j] = True
                    elif dp[i][j-1] is True and p[i-2] == '.':
                        dp[i][j] = True
                    elif dp[i-2][j] is True:
                        dp[i][j] = True
                    elif dp[i-1][j-1] is True and (p[i-2] == s[j-1] or
                                                   p[i-2] == '.'):
                        dp[i][j] = True
                elif j >= 1 and dp[i-1][j-1] is True and p[i-1] == s[j-1]:
                    dp[i][j] = True
        return dp[-1][-1]
        
# Solution Code2
class Solution:
    def isMatch(self, s, p):
        mem = {}
        def _isMatch(i, j):
            if (i, j) not in mem:
                if j == len(p):
                    result = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in (s[i], '.')
                    if j + 1 < len(p) and p[j+1] == '*':
                        result = _isMatch(i, j+2) or (first_match and _isMatch(i+1, j))
                    else:
                        result = first_match and _isMatch(i+1, j+1)
                mem[i, j] = result
            return mem[i, j]

        return _isMatch(0,0)

        
if __name__ == "__main__":
    s = "baccbbcbcacacbbc"
    p = "c*.*b*c*ba*b*b*.a*"
    print(Solution().isMatch(s, p))
    
# Solution Code3:调用re API
import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return re.match(p+'$', s)
 
