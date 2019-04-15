# 题目
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
# 例如，给出 n = 3，生成结果为：
#   [
#     "((()))",
#     "(()())",
#     "(())()",
#     "()(())",
#     "()()()"
#   ]

# Solution Code
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return list()
        if n == 1:
            return ["()"]
        res = set()
        tmp = self.generateParenthesis(n-1)
        for s in tmp:
            for i in range(len(s)):
                tmp = s[:i] + "()" + s[i:]
                res.add(tmp)
                
        return list(res)
