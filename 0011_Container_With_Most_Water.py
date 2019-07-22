# 盛最多水的容器
# 题目:
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 说明：你不能倾斜容器，且 n 的值至少为 2。

# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

# 示例:
#   输入: [1,8,6,2,5,4,8,3,7]
#   输出: 49

# Solution Code
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0  # x坐标轴上，左边点的横坐标
        right = len(height) - 1  # x坐标轴上，右边点的横坐标
        maxArea = 0  # 最大面积，初始为0
        while left < right:
            b = right - left # 边长 = 横坐标之差
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            area = b*h
            if maxArea < area:
                maxArea = area
        return maxArea
