"""
560. 和为 K 的子数组
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
子数组是数组中元素的连续非空序列。
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 1.双重遍历（超时）
        # flag = False
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if not flag and sum(nums[i:j + 1]) == k:
        #             count += 1
        #             flag = True
        #             temp = j+1
        #         if flag and temp != j+1 and sum(nums[temp:j+1]) == 0:
        #             count += 1
        #             temp = j+1
        #     temp = 0
        #     flag = False
        # return count
        # 2.前缀和
        # nums_sum = [0 for _ in range(len(nums))]
        # nums_sum[0] = nums[0]
        # for i in range(1, len(nums)):
        #     nums_sum[i] = nums_sum[i - 1] + nums[i]
        # count = 0
        # for i in range(0, len(nums_sum)):
        #     if nums_sum[i] == k:
        #         count += 1
        #     for j in range(i+1, len(nums_sum)):
        #         if nums_sum[j] - nums_sum[i] == k:
        #             count += 1
        # return count
        # 3.前缀和+哈希表
        hashmap = {0: 1}
        pre = 0
        count = 0
        for i in range(0, len(nums)):
            pre += nums[i]
            if pre - k in hashmap:
                count += hashmap[pre - k]
            if pre in hashmap:
                hashmap[pre] += 1
            else:
                hashmap[pre] = 1
        return count


sol = Solution()
nums1 = [1, 1, 1]
k1 = 2
nums2 = [1, -1, 0]
k2 = 0
nums3 = [3, 4, 7, 2, -3, 1, 4, 2]
k3 = 7
print(sol.subarraySum(nums3, k3))
