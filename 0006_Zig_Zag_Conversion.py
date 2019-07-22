# Z 字形变换
#  题目：
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "LEETCODEISHIRING"行数为 3 时，排列如下：

# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
# 请你实现这个将字符串进行指定行数变换的函数：
# string convert(string s, int numRows);
# 示例 1:
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"

# 示例 2:
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"

# 解释:
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G

# 解题：示例 1
# s = "LEETCODEISHIRING", numRows = 3
# s_rows = ["", "", ""]
# s_len = len(s)=16
# loop_len = 2*numRows-2 = 2*3-2=4
# ref_num:
# 0%4=0   4%4=0   8%4=0    12%4=0
# 1%4=1   5%4=1   9%4=1    13%4=1
# 2%4=2   6%4=2   10%4=2   14%4=2
# 3%4=3   7%4=3   11%4=3   15%4=3
# if ref_num >= 3:
#     ref_num = 2 * 3 - 3 -2 = 1

# s_rows:
# 0:  L C I R
# 1:  E O S I
# 2:  E D H N
# 1:  T E I G
# 拼接起来的结果：LCIRETOESIIGEDHN

# Solution
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        s_rows = [""] * numRows
        s_len = len(s)
        loop_len = 2*numRows-2
        for i in range(s_len):
            ref_num = i % loop_len
            if ref_num >= numRows:
                ref_num = 2*numRows-ref_num-2
            s_rows[ref_num]+=s[i]
        return "".join(s_rows)


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zigzag-conversion
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
