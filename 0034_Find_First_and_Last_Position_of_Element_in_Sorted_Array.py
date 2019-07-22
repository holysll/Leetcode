# 在排序数组中查找元素的第一个和最后一个位置
# 题目：
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 你的算法时间复杂度必须是O(log n) 级别。
# 如果数组中不存在目标值，返回 [-1, -1]。

# 示例 1:
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]

# 示例 2:
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# <暴力二次线性扫描法>
# 首先，我们对 nums 数组从左到右做线性遍历，当遇到 target 时中止。
# 如果我们没有中止过，那么 target 不存在，我们可以返回“错误代码” [-1, -1] 。
# 如果我们找到了有效的左端点坐标，我们可以坐第二遍线性扫描，但这次从右往左进行。
# 这一次，第一个遇到的 target 将是最右边的一个（因为最左边的一个存在，所以一定会有一个最右边的 target）。
# 我们接下来只需要返回这两个坐标。

# 但是，算法时间复杂度为： O(n)

# Solution 1
class Solution(object):        
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 找到出现target时最左边的下标，如果未出现返回[-1,-1]
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # 找到出现target时最右边边的下标，逆向
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]
 
 
 # <二分查找法>
# 总体算法工作过程与线性扫描方法类似，除了找最左和最右下标的方法。
# 这里我们仅仅做几个微小的调整，用这种修改过的二分查找方法去搜索这个排过序的数组。
# 首先，为了找到最左边（或者最右边）包含 target 的下标（而不是找到的话就返回 true ），所以算法在我们找到一个 target 后不能马上停止。
# 我们需要继续搜索，直到 lo == hi 且它们在某个 target 值处下标相同。

# 另一个改变是 left 参数的引入，它是一个 boolean 类型的变量，指示我们在遇到 target == nums[mid] 时应该做什么。
# 如果 left 为 true ，那么我们递归查询左区间，否则递归右区间。
# 考虑如果我们在下标为 i 处遇到了 target ，最左边的 target 一定不会出现在下标大于 i 的位置，所以我们永远不需要考虑右子区间。
# 当求最右下标时，道理同样适用。
# 由于二分查找每次将搜索区间大约划分为两等分，所以时间复杂度为： O(log n)

# Solution 2
class Solution(object):
    # 返回最左边(或最右边)包含 target 的下标
    # 对数组nums进行二分查找
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_idx = self.extreme_insertion_index(nums, target, True)

        # 确定左边在nums数组边界内
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]
