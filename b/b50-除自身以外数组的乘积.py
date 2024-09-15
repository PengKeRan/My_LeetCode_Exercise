# 238. 除自身以外数组的乘积
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# todo:请不要使用除法，且在 O(n) 时间复杂度内完成此题。


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 超时
        # n = len(nums)
        # ans = [1 for _ in range(n)]
        # for i in range(n):
        #     temp = [nums[i] for _ in range(n)]
        #     temp[i] = 1
        #     for j in range(n):
        #         if ans[j] != 0:
        #             ans[j] *= temp[j]
        # return ans

        n = len(nums)
        prefix = [1 for _ in range(n)]
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] *= prefix[i-1] * nums[i]
        suffix = [1 for _ in range(n)]
        suffix[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix[i] *= suffix[i+1] * nums[i]
        print(prefix)
        print(suffix)
        ans = [1 for _ in range(n)]
        ans[0] = suffix[1]
        ans[-1] = prefix[-2]
        for i in range(1,n-1):
            ans[i] = prefix[i-1] * suffix[i+1]
        return ans


sol = Solution()
nums = [1, 2, 3, 4]
print(sol.productExceptSelf(nums)) # [24,12,8,6]
