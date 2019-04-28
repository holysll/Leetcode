# 题目
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 必须原地修改，只允许使用额外常数空间。
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
#   1,2,3 → 1,3,2
#   3,2,1 → 1,2,3
#   1,1,5 → 1,5,1

# Solution Code
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = r = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
            
        i -= 1
        if i >= 0:
            while j >= i and nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
            
        i += 1      
        while i < r:
            nums[i], nums[r] = nums[r], nums[i]
            i += 1
            r -= 1
            
if __name__ == "__main__":
    nums = [3,2,1]
    Solution().nextPermutation(nums)
    print(nums)
