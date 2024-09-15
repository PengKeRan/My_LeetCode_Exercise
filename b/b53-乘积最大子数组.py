# 152. 乘积最大子数组
# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组
# （该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 测试用例的答案是一个 32-位 整数。


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp_max = list(nums)
        dp_min = list(nums)
        for i in range(1, n):
            dp_max[i] = max(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
        return max(max(dp_max), max(dp_min))


sol = Solution()
nums = [2,3,-2,4]
print(sol.maxProduct(nums))
