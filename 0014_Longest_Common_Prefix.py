# 最长公共前缀
# 题目描述：
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"

# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。

# 说明:
# 所有输入只包含小写字母 a-z 。

# Solution code1：
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        dic = {}
        for i  in range(len(strs)):
            dic[i] = strs[i]
        mins = 1000
        for j in dic:
            if len(dic[j]) <mins:
                mins = len(dic[j])
        tem = []
        for i in range(mins):
            res = []
            for j in dic:
                res.append(dic[j][i])
            res  = set(res)
            if len(res) == 1:
                res = list(res)
                tem.append(res[0])
            else:
                break
        return "".join(tem)


# Solution Code2:
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minL = float('inf')
        res = ''
        if not strs:
            return res
        for i in range(len(strs)):
            minL = min(minL, len(strs[i]))
        for i in range(minL):
            tag = 0
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    tag = 1
                    break
            if not tag:
                res += strs[0][i]
            else:
                break
        return res

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-common-prefix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
