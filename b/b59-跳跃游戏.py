# 55.跳跃游戏
# 给你一个非负整数数组  ，你最初位于数组的
# 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。nums
# 判断你是否能够到达最后一个下标，如果可以，返回 ；否则，返回 。truefalse

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        n = len(nums)
        for i in range(n):
            reach = max(reach, i + nums[i])
            if i == reach:
                break
        if reach >= n - 1:
            return True
        return False


sol = Solution()
nums = [3, 2, 1, 0, 4]
print(sol.canJump(nums))
