# 209. 长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其总和大于等于 target 的长度最小的 子数组
#  [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = n + 1
        left = 0
        right = 0
        cur_sum = 0
        while right < n:
            cur_sum += nums[right]
            while cur_sum >= target:
                res = min(res, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            right += 1
        return res if res <= n else 0

        # n = len(nums)
        # min_len = n + 1
        # window = []
        # cur_sum = 0
        # i = 0
        # while i < n:
        #     if cur_sum < target:
        #         window.append(nums[i])
        #         cur_sum += nums[i]
        #         i += 1
        #     while cur_sum >= target:
        #         min_len = min(min_len, len(window))
        #         if min_len == 1:
        #             return min_len
        #         cur_sum -= window.pop(0)
        # return min_len if min_len <= n else 0


nums = [1, 2, 3, 4, 5]
target = 15
sol = Solution()
print(sol.minSubArrayLen(target, nums))
