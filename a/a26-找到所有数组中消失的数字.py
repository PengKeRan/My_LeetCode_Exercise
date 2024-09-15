# 448. 找到所有数组中消失的数字
# 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
# 请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
# 进阶：你能在不使用额外空间且时间复杂度为 O(n) 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        for i in range(n):
            x = (nums[i] - 1) % n
            nums[x] += n
        for i in range(len(nums)):
            if nums[i] <= n:
                res.append(i + 1)
        return res

sol = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(sol.findDisappearedNumbers(nums))
