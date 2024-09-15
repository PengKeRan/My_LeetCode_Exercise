"""
312. 戳气球
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组nums中。
现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。
这里的 i - 1 和 i + 1 代表和i相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
求所能获得硬币的最大数量。
"""


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for k in range(2, len(nums)):
            for i in range(0, len(nums) - k):
                j = i + k
                for m in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][m] + dp[m][j] + nums[i] * nums[m] * nums[j])
        # for d in dp:
        #     print(d)
        return dp[0][-1]


sol = Solution()
num1 = [3, 1, 5, 8]
num2 = [1, 5]
nums3 = [35, 16, 83, 87, 84, 59, 48, 41]
print(sol.maxCoins(num1))
# print(sol.maxCoins(num2))
print(sol.maxCoins(nums3))
