"""
31.下一个排列
整数数组的一个 排列就是将其所有成员以序列或线性顺序排列。
例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。
更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。
如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。

必须 原地 修改，只允许使用额外常数空间。
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i + 1
                for j in range(i + 1, len(nums)):
                    if nums[j] - nums[i] <= nums[i + 1] - nums[i] and nums[j] > nums[i]:
                        index = j
                temp = nums[index]
                nums[index] = nums[i]
                nums[i] = temp
                if len(nums) - i - 1 == 1:
                    return
                for k in range(0, (len(nums) - i - 1) // 2):
                    temp = nums[i + 1 + k]
                    nums[i + 1 + k] = nums[len(nums) - 1 - k]
                    nums[len(nums) - 1 - k] = temp
                return
        length = len(nums)
        for i in range(0, length // 2):
            temp = nums[i]
            nums[i] = nums[length - 1 - i]
            nums[length - 1 - i] = temp
        return


nums1 = [5, 4, 7, 5, 3, 2]
# nums2 = [3, 2, 1]
# nums3 = [2, 3, 1]
# nums4 = [2, 4, 3, 1]
sol = Solution()
sol.nextPermutation(nums1)
# sol.nextPermutation(nums2)
# sol.nextPermutation(nums3)
# sol.nextPermutation(nums4)
print(nums1)  # 132
# print(nums2)  # 123
# print(nums3)  # 312
# print(nums4)  # 3124

#  1234
#  1243
#  1324
#  1342
#  1423
#  1432
#  2134
#  2143
#  2314
#  2341
#  2413
#  2431
#
#
#
#
