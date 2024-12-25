# 128. 最长连续序列
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        res = 1 if n > 0 else 0
        temp = res
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                temp += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                res = max(res, temp)
                temp = 1
        return max(res, temp)


n = [1, 2, 0, 1]
sol = Solution()
print(sol.longestConsecutive(n))
