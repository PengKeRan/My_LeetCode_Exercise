"""
215.数组中的第K个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""


class Solution(object):
    def findKthLargest(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # arr = sorted(nums, reverse=True)
        # return arr[k-1]
        # 1.快速排序
        self.quickSort(arr, 0, len(arr) - 1)
        return arr[-k]

    # 快速排序
    def quickSort(self, arr, left, right):
        if left < right:
            index = self.split(arr, left, right)
            self.quickSort(arr, left, index - 1)
            self.quickSort(arr, index + 1, right)

    def split(self, arr, left, right):
        # 以最右边的为中间值
        mid = arr[right]
        while left < right:
            while left < right and arr[left] < mid:
                left += 1
            arr[right] = arr[left]
            while left < right and arr[right] >= mid:
                right -= 1
            arr[left] = arr[right]
        arr[left] = mid
        return left


sol = Solution()
nums1 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k1 = 2
print(sol.findKthLargest(nums1, k1))
