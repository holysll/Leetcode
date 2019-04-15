# 题目
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 注意：
# 答案中不可以包含重复的四元组。

# 示例：
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 满足要求的四元组集合为：
#   [
#     [-1,  0, 0, 1],
#     [-2, -1, 1, 2],
#     [-2,  0, 0, 2]
#   ]

# Solution Code
nums.sort()
        result = list()
        nums_len = len(nums)
        if nums_len < 4:
            return result
        
        if nums[0] * 4 > target or nums[nums_len - 1] * 4 < target:
            return result

        nums_map = {}
        for i in range(nums_len-1, 0, -1):
            if i < nums_len - 1 and nums[i] == nums[i + 1]:
                continue
            for j in range(i-1, -1, -1):
                if j < i-1 and nums[j] == nums[j + 1]:
                    continue
                if nums[i] + nums[j] not in nums_map:
                    nums_map[nums[i] + nums[j]] = [[j, i]]
                else:
                    nums_map[nums[i] + nums[j]].append([j, i])

        for i in range(nums_len - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, nums_len - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                dif = target - nums[i] - nums[j]
                if dif not in nums_map:
                    continue
                else:
                    for num in nums_map[dif]:
                        if num[0] > j:
                            result.append([nums[i], nums[j], nums[num[0]], nums[num[1]]])
        return result
