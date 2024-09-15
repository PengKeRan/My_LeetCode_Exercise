"""
136.只出现一次的数字
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # d = dict()
        # for i in range(len(nums)):
        #     if d.get(nums[i]) is None:
        #         d[nums[i]] = 0
        #     d[nums[i]] += 1
        #     if d.get(nums[i]) == 2:
        #         d[nums[i]] = 0
        # for k, v in d.items():
        #     if v == 1:
        #         return k

        # 异或运算
        single = 0
        for num in nums:
            single ^= num
        return single


nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
nums3 = [-1]
sol = Solution()
print(sol.singleNumber(nums1))  # 1
print(sol.singleNumber(nums2))  # 4
print(sol.singleNumber(nums3))  # -1
