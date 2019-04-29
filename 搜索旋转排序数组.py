# 题目
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 你可以假设数组中不存在重复的元素。
# 你的算法时间复杂度必须是 O(log n) 级别。

# 示例 1:
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4

# 示例 2:
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1

# Solution Code1
class Solution(object):
    def core(self,a,i,j,t):
        if i>j:
            return -1
        m=(i+j)/2
        if a[m]==t:
            return m
        if a[m]>=a[i] and a[m]<=a[j]:
            if a[m]<t:
                return self.core(a,m+1,j,t)
            else:
                return self.core(a,i,m-1,t)
        elif a[m]<a[i]:
            if a[m]>t:
                return self.core(a,i,m-1,t)
            else:
                if a[j]==t:
                    return j
                elif a[j]<t:
                    return self.core(a,i,m-1,t)
                else:
                    return self.core(a,m+1,j,t)
        else:
            if a[m]<t:
                return self.core(a,m+1,j,t)
            else:
                if a[i]==t:
                    return i
                elif a[i]<t:
                    return self.core(a,i,m-1,t)
                else:
                    return self.core(a,m+1,j,t)
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        return self.core(nums,0,len(nums)-1,target)

    
# Solution Code2    
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid
                else:
                    high = mid - 1

        return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(Solution().search(nums, target))
