# 题目
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

# 示例:
#   输入："23"
#   输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

# Solution Code1
import itertools
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        l_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
                 '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        chars = [l_map.get(d) for d in digits]
        return [''.join(x) for x in itertools.product(*chars)]


if __name__ == '__main__':
    digits = '23'
    print(Solution().letterCombinations(digits))
    
# Sulution Code2
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2':['a','b','c'], '3':['d','e','f'], 
                   '4':['g','h','i'], '5':['j','k','l'],
                   '6':['m','n','o'], '7':['p','q','r','s'],
                   '8':['t','u','v'], '9':['w','x','y','z']}
        temp = ['']
        ans = []
        for d in digits:
            ans = []
            for char in temp:
                for new_char in mapping[d]:
                    ans.append(char+new_char)
            temp = ans
        return ans

if __name__ == '__main__':
    digits = '23'
    print(Solution().letterCombinations(digits))
