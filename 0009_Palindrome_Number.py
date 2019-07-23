# 回文数
# 题目：
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 示例 1:
# 输入: 121
# 输出: true

# 示例 2:
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

# 示例 3:
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。

# 进阶:
# 你能不将整数转为字符串来解决这个问题吗？

# Solution code1(转换为字符串，翻转)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

    
# Solution code2(通过% 和 //判断):

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 特殊情况：
        # 如上所述，当 x < 0 时，x 不是回文数。
        # 同样地，如果数字的最后一位是 0，为了使该数字为回文，则其第一位数字也应该是 0，只有 0 满足这一属性
        if x < 0 or (x !=0 and x % 10 == 0):
            return False
        y = 0
        while x > y:
            y = 10 * y + x % 10
            x //= 10
        # 当数字长度为奇数时，我们可以通过 y//10 去除处于中位的数字。
        # 例如，当输入为 12321 时，在 while 循环的末尾我们可以得到 x = 12，y = 123，
        # 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
        return x == y or x == y // 10
    
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
