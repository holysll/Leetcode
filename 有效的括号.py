# 题目
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
#   左括号必须用相同类型的右括号闭合。
#   左括号必须以正确的顺序闭合。
#   注意空字符串可被认为是有效字符串。

# 示例 1:
#   输入: "()"
#   输出: true

# 示例 2:
#   输入: "()[]{}"
#   输出: true

# 示例 3:
#   输入: "(]"
#   输出: false

# 示例 4:
#   输入: "([)]"
#   输出: false

# 示例 5:
#   输入: "{[]}"
#   输出: true

# Solution Code
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 用数据结构表示栈的时候，可以采用数组或者链表，数组相对实现比较简单
        # 定义一个空数组做栈，通过append()和pop()以及len()方法来模仿入栈出栈，栈的大小
        stack = []
        # 定义一个数组，用做查找元素
        m = ["()","[]","{}"]
        # 遍历字符串每一个元素入栈
        for i in range(0, len(s)):
            # 然后将每个元素入栈
            stack.append(s[i])
            # 当遇到栈的大小超过2时，并且栈中最后两个元素用作查找元素数组是，就弹出栈的最上面两个元素
            if len(stack) >= 2 and stack[-2]+stack[-1] in m:
                stack.pop()
                stack.pop()
        # 当for循环遍历完之后，判断此时栈中元素时候完全弹出，如果是就返回True
        return len(stack) == 0
result = Solution()
shili1 = result.isValid('()')
shili2 = result.isValid('()[]{}')
shili3 = result.isValid('(]')
shili4 = result.isValid('([)]')
shili5 = result.isValid('{[]}')
print(shili1,shili2,shili3,shili4,shili5)

# 官方解答:哈希映射
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
