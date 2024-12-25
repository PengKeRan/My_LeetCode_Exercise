# 219. 存在重复元素 II
class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        memo = dict()
        for i in range(n):
            temp = nums[i]
            if temp in memo.keys() and i - memo[temp] <= k:
                return True
            memo[temp] = i

        return False
