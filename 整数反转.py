# 题目：
#   给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

# 示例 1:
#   输入: 123
#   输出: 321

# 示例 2:
#   输入: -123
#   输出: -321

# 示例 3:
#   输入: 120
#   输出: 21

# 注意:
#   假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

# Solution Code:
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        str_x = str(x) # 把整数x转化为字符串
        x = ''
        if str_x[0] == '-':
            x += '-'
        x += str_x[len(str_x)-1::-1].lstrip("0").rstrip("-") # 左删除0，有删除负号
        x = int(x)  # 再把x转化为整型
        if -2**31 < x < 2**31-1:
            return x
        return 0
