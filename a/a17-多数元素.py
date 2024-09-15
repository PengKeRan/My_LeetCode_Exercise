"""
169. 多数元素
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """




        
        return sorted(nums)[len(nums)//2]


sol = Solution()
nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(sol.majorityElement(nums1))
print(sol.majorityElement(nums2))
