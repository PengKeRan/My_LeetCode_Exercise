# 228. 汇总区间
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        if n == 0:
            return []
        res = []
        start = nums[0]
        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                res.append(
                    f"{start}->{nums[i - 1]}" if start != nums[i - 1] else str(start)
                )
                start = nums[i]

        res.append(f"{start}->{nums[-1]}" if start != nums[-1] else str(start))
        return res


nums = [-2147483648, -2147483647, 2147483647]
sol = Solution()
print(sol.summaryRanges(nums))
