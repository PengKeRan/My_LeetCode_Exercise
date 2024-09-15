"""
239.滑动窗口最大值
给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。
"""


class MyQueue:
    def __init__(self):
        self.queue = []

    def pop(self, value):
        if self.queue and self.queue[0] == value:
            self.queue.pop(0)

    def push(self, value):
        if self.queue == []:
            self.queue.append(value)
            return
        while self.queue and self.queue[-1] < value:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        if self.queue:
            return self.queue[0]


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 2.单调队列
        # myQueue = MyQueue()
        # res = []
        # for i in range(k):
        #     myQueue.push(nums[i])
        # res.append(myQueue.front())
        # for i in range(k, len(nums)):
        #     myQueue.pop(nums[i-k])
        #     myQueue.push(nums[i])
        #     res.append(myQueue.front())
        # return res

        # 1.时间复杂度过高
        # if len(nums) == k:
        #     return [max(nums)]
        # res = []
        # max_value = max(nums[0:k])
        # res.append(max_value)
        # for j in range(k, -1, -1):
        #     if nums[j] == max_value:
        #         max_index = j
        # for i in range(k, len(nums)):
        #     if i - max_index > k - 1:
        #         max_value = max(nums[i - k + 1:i + 1])
        #         res.append(max_value)
        #         for j in range(i, i - k, -1):
        #             if nums[j] == max_value:
        #                 max_index = j
        #     elif nums[i] >= max_value:
        #         max_value = nums[i]
        #         res.append(max_value)
        #         max_index = i
        #     else:
        #         res.append(max_value)
        # return res


sol = Solution()
nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
k1 = 3
nums2 = [1]
k2 = 1
print(sol.maxSlidingWindow(nums1, k1))  # [3,3,5,5,6,7]
print(sol.maxSlidingWindow(nums2, k2))
