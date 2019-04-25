# 题目
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 返回被除数 dividend 除以除数 divisor 得到的商。

# 示例 1:
# 输入: dividend = 10, divisor = 3
# 输出: 3

# 示例 2:
# 输入: dividend = 7, divisor = -3
# 输出: -2

# 说明:
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

# 思路
# 用减法实现除法不就好了，python刷题实现甚至可以直接使用range()来实现除法，需要注意的点如下：
# 1.提前判断结果的正负号
# 2.结果在[-2**31，2**31-1]中，要判断结果是否移除
# 3.使用range()来计算除法时，一旦除法可以整除我们要对结果+1，因为len(range(3,7,3))的结果是2，len(range(3,9,3))的结果也是2

# Solution Code
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        below = 1
        if dividend < 0 <divisor or divisor < 0 < dividend:
            below = - 1
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0
        elif divisor == 1:
            result = dividend * below
            if result >= 2**31-1:
                return 2**31-1
            return result
        result = len(xrange(divisor, dividend, divisor))
        if (result+1)*divisor == dividend:
            result += 1
        return result*below
