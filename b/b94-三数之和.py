# 15. 三数之和
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    if [nums[i], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < n and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while right > 0 and nums[right] == nums[right + 1]:
                        right -= 1
                elif total > target:
                    right -= 1
                else:
                    left += 1
        return res


sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums))
