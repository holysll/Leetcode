# 字符串转换整数 (atoi)
# 题目：
# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
# 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
# 在任何情况下，若函数不能进行有效的转换时，请返回 0。

# 说明：
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31,  2^31 − 1]。
# 如果数值超过这个范围，请返回  INT_MAX (2^31 − 1) 或 INT_MIN (−2^31) 。

# 示例 1:
# 输入: "42"
# 输出: 42

# 示例 2:
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

# 示例 3:
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

# 示例 4:
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。

# 示例 5:
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
     因此返回 INT_MIN (−231) 。


# Solution Code1:(正则解法)
# 使用正则表达式：
# ^：匹配字符串开头
# [\+\-]：代表一个+字符或-字符
# ?：前面一个字符可有可无
# \d：一个数字
# +：前面一个字符的一个或多个
# \D：一个非数字字符
# *：前面一个字符的0个或多个
# max(min(数字, 2**31 - 1), -2**31) 用来防止结果越界

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1), -2**31)
        
# Solution Code2:(正则解法)        
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.lstrip()
        try:
            result =  int(re.match("[-+]?[0-9]\d*",s).group())
            if result >  2147483647 : return 2147483647
            if result < -2147483648 : return -2147483648
            return result
        except:
            return 0
        
# Solution Code3:(双指针解法)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.strip()#去除空格
        if str=="" :return 0;#特殊情况 str="0"
        left=0;right=0
        maxi=2147483647;mini=-2147483648#用于后面判断是否越界
        if str[0]=='+' or str[0]=='-': left=1#判断第一个字符是否为正负号
        if (left==1 and len(str)==1) or str[left]<'0' or str[left]>'9': return 0#注意特殊情况 str="+"
        for i in range(left,len(str)):#right移动到第一个不是数字的地方
            if str[i]>='0' and str[i]<='9':
                right=i
            else:
                break
        res=str[left:right+1].lstrip('0')#去除左边的0
        if len(res)==0:return 0#清除后可能没数字
        else :res=eval(res)#eval是个非常好用的函数，自行了解
        if left==1 and str[0]=='-':#判断正负
            res=-res
        if res>maxi: return maxi
        elif res<mini: return mini
        else :return res
 
# Solution Code4:(常规if else判断)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        answer = 0
        minus = False
        num_space = 0
        
        # 判断字符串前面的空格数，并清空
        for c in str:
            if c == ' ':
                num_space += 1
            else:
                break
        new_str = str[num_space:]
        
        if len(new_str) == 0:
            return 0
        
        # 判断第一位的正负号
        if new_str[0] == '+':
            new_str = new_str[1:]
        elif new_str[0] == '-':
            minus = True
            new_str = new_str[1:]
        
        # 判断后面的字符
        for c in new_str:
            if '0' <= c <= '9':
                answer = 10 * answer + int(c)
            else:
                break
        
        if minus:
            answer = -answer
        if answer > 2**31 -1:
            return 2**31 -1
        elif answer < -2**31:
            return -2**31
        else:
            return answer
            

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-to-integer-atoi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
