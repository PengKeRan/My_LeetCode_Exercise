# 1. 两数之和
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        memo = dict()
        for i in range(n):
            if target - nums[i] not in memo.keys():
                memo[nums[i]] = i
            else:
                return [i, memo[target - nums[i]]]

        return None


nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))
