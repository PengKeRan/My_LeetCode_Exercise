"""
34. 在排序数组中查找元素的第一个和最后一个位置

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        middle = 0
        while left < right - 1:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle
            if nums[middle] > target:
                right = middle
            if nums[middle] == target:
                break
        if left == right - 1:
            middle = left if nums[left] == target else right
        for i in range(0, middle+1):
            if nums[middle - i] == target:
                left = middle - i
        for j in range(0, len(nums)-middle):
            if nums[middle + j] == target:
                right = middle + j
        return [left, right]


sol = Solution()
nums1 = [7]
target1 = 7
print(sol.searchRange(nums1, target1))
