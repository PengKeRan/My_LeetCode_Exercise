"""
494.目标和
给你一个整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加'+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
"""


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sum_all = 0
        for num in nums:
            sum_all += num
        if (sum_all - target) % 2 != 0 or sum_all < target:
            return 0
        neg = (sum_all - target) // 2
        dp = [[0 for _ in range(neg + 1)] for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            num = nums[i - 1]
            for j in range(neg + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
        return dp[len(nums)][neg]

        # 超时
        # if len(nums) == 1:
        #     return 1 if abs(nums[0]) == abs(target) else 0
        # count = 0
        #
        # def mySum(arr):
        #     s = []
        #     if len(arr) == 1:
        #         s.append(arr[0])
        #         s.append(-arr[0])
        #         return s
        #     for val in mySum(arr[1:len(arr)]):
        #         s.append(arr[0] + val)
        #         s.append(-arr[0] + val)
        #     return s
        #
        # res = mySum(nums)
        # for val in res:
        #     count += 1 if val == target else 0
        # return count


sol = Solution()
nums1 = [2, 107, 109, 113, 127, 131, 137, 3, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 47, 53]

target1 = 1000
nums2 = [1]
target2 = 1
print(sol.findTargetSumWays(nums1, target1))  # 5
# print(sol.findTargetSumWays(nums2, target2))
