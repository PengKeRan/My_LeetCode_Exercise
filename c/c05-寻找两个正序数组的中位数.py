"""
4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。
"""
import numpy as np


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return np.median(nums1+nums2)
        # if len(nums2) == 0:
        #     return np.median(nums1)
        # if len(nums1) == 0:
        #     return np.median(nums2)
        # i = 0
        # j = 0
        # pos = 0
        # target = (len(nums1) + len(nums2)) // 2
        # while i < len(nums1) and j < len(nums2):
        #     if pos == target:
        #         print(pos)
        #         print(i)
        #         print(j)
        #         if (len(nums1) + len(nums2)) % 2 != 0:
        #             return min(nums1[i], nums2[j])
        #         else:
        #             return (nums1[i] + nums2[j]) / 2
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     else:
        #         j += 1
        #     pos += 1
        #
        # if i < len(nums1):
        #     if pos == target:
        #         return min(nums1[i], nums2[-1]) if (len(nums1) + len(nums2)) % 2 != 0 else (nums1[i] + nums2[-1]) / 2
        #     for m in range(len(nums1[i:])):
        #         if pos == target:
        #             return nums1[m] if (len(nums1) + len(nums2)) % 2 != 0 else (nums1[m] + nums1[m + 1]) / 2
        #         pos += 1
        #
        # if j < len(nums2):
        #     if pos == target:
        #         return min(nums2[j], nums1[-1]) if (len(nums1) + len(nums2)) % 2 != 0 else (nums2[j] + nums1[-1]) / 2
        #     for m in range(len(nums2[j:])):
        #         if pos == target:
        #             return nums2[m] if (len(nums1) + len(nums2)) % 2 != 0 else (nums2[m] + nums2[m + 1]) / 2
        #         pos += 1


sol = Solution()
nums1 = [0, 0, 0, 0, 0]
nums2 = [-1, 0, 0, 0, 0, 0, 1]
nums2_1 = [1, 2]
nums2_2 = [3, 4]
print(sol.findMedianSortedArrays(nums1, nums2))
# print(sol.findMedianSortedArrays(nums2_1, nums2_2))
