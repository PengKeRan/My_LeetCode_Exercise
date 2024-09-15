"""
15.三数之和
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 双指针+排序
        res = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if nums[i] > 0 or (i >= 1 and nums[i] == nums[i - 1]):
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right and nums[right] >= 0:
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
        return res

        # 超时
        # pos = []
        # neg = []
        # zeros = []
        # res = []
        # for num in nums:
        #     if num == 0:
        #         zeros.append(num)
        #     elif num > 0:
        #         pos.append(num)
        #     else:
        #         neg.append(num)
        # pos = sorted(pos)
        # neg = sorted(neg)
        # # 有0的情况
        # if zeros:
        #     if len(zeros) >= 3:
        #         res.append([0, 0, 0])
        #     for i in range(len(neg)):
        #         if i > 0 and neg[i] == neg[i - 1]:
        #             continue
        #         if -neg[i] in pos:
        #             res.append([neg[i], -neg[i], 0])
        # # 除开0的情况
        # if pos == [] or neg == []:
        #     return res
        # # 1.负数target
        # for k in range(len(neg)):
        #     if neg[k] == -1:
        #         continue
        #     if k >= 1 and neg[k] == neg[k - 1]:
        #         continue
        #     target = abs(neg[k])
        #     # 在正数数组中找和为target的两个数
        #     for i in range(len(pos) - 1):
        #         if i >= 1 and pos[i] == pos[i - 1]:
        #             continue
        #         for j in range(len(pos) - 1, i, -1):
        #             # if j <= len(pos) - 2 and pos[j] == pos[j + 1]:
        #             #     continue
        #             if pos[i] + pos[j] == target:
        #                 res.append([pos[i], pos[j], -target])
        #                 break
        #
        # # 2.正数target
        # for k in range(len(pos)):
        #     if pos[k] == 1:
        #         continue
        #     if k >= 1 and pos[k] == pos[k - 1]:
        #         continue
        #     target = -pos[k]
        #     # 在负数数组中找和为target的两个数
        #     for i in range(len(neg) - 1):
        #         if i >= 1 and neg[i] == neg[i - 1]:
        #             continue
        #         for j in range(len(neg) - 1, i, -1):
        #             # if j <= len(pos) - 2 and pos[j] == pos[j + 1]:
        #             #     continue
        #             if neg[i] + neg[j] == target:
        #                 res.append([neg[i], neg[j], -target])
        #                 break
        # return res


sol = Solution()
nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [1, -5, -2, -2, -2, -4, -4, -4, 4, 0, 4, 0, 3, 1, -5, 0]
nums3 = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
print(sol.threeSum(nums2))
