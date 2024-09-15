"""
1. 两数之和
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    arr = []
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > 0 and nums[j] > 0:
                if nums[i] > target or nums[j] > target:
                    continue
            if nums[i] < 0 and nums[j] < 0:
                if nums[i] < target or nums[j] < target:
                    continue
            if nums[i] + nums[j] == target:
                arr.append(i)
                arr.append(j)
                return arr


print(twoSum([3, 2, 4], 6))
