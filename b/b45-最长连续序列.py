# 128. 最长连续序列
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                current = num
                current_len = 1
                while current+1 in nums:
                    current = current + 1
                    current_len += 1
                longest = max(longest, current_len)
        return longest


sol = Solution()
nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(sol.longestConsecutive(nums1))
# print(sol.longestConsecutive(nums2))
