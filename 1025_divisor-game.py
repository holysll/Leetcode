# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-24 12:02
# software: PyCharm
"""
题目：除数博弈
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

示例 1：

输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。
示例 2：

输入：3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
 

提示：

1 <= N <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divisor-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages
import sys

# 数学归纳法
"""
基本思路：

最终结果应该是占到 2 的赢，占到 1 的输；

若当前为奇数，奇数的约数只能是奇数或者 1，因此下一个一定是偶数；

若当前为偶数， 偶数的约数可以是奇数可以是偶数也可以是 1，因此直接减 1，则下一个是奇数；

因此，奇则输，偶则赢。直接:

作者：pandawakaka
链接：https://leetcode-cn.com/problems/divisor-game/solution/python3gui-na-fa-by-pandawakaka/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N % 2 == 0


# 动态规划
class Solution1(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        dp = [0 for i in range(N + 1)]
        dp[1] = 0  # 如果爱丽丝抽到1，则输
        if N <= 1:
            return False
        else:
            dp[2] = 1  # 如果爱丽丝抽到2，则赢
            for i in range(3, N + 1):
                for j in range(1, i // 2):
                    # 若j是i的余数且dp[i-j]==0，则代表当前为真
                    if i % j == 0 and dp[i - j] == 0:
                        dp[i] = 1
                        break
            return dp[N] == 1


# 深度优先DFS递归
class Solution2(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        res = {}
        def dfs(N):
            if N == 1:
                return False
            if N in res:
                return res[N]
            res[N] = any(not dfs(N-i) for i in range(1, N//2+1) if N%i == 0)
            return res[N]
        return dfs(N)

if __name__ == '__main__':
    N = 3
    solution = Solution()
    res = solution.divisorGame(N)
    print(res)

    solution1 = Solution1()
    res1 = solution1.divisorGame(N)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.divisorGame(N)
    print(res2)
