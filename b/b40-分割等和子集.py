"""
416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2

        # 二维数组-背包问题
        # dp = [[0 for _ in range(target+1)] for _ in range(len(nums))]
        # for i in range(0, len(dp)):
        #     for j in range(0, target+1):
        #         if nums[i] > j:
        #             dp[i][j] = dp[i - 1][j]
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
        #
        # return dp[-1][-1] == target

        # 滚动数组方法：将二维数组压缩到一维数组
        dp = [0 for _ in range(target + 1)]
        for i in range(len(nums)):
            for j in range(len(dp) - 1, -1, -1):
                if nums[i] <= j:
                    dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        print(dp)
        return dp[-1] == target


sol = Solution()
nums1 = [1, 5, 11, 5]
print(sol.canPartition(nums1))
