"""
11.盛最多水的容器
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。

说明：你不能倾斜容器。
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = min(height[right], height[left]) * (right - left)

        while left < right:
            if height[left] < height[right]:
                left += 1
                if height[left] < height[left - 1]:
                    continue
            else:
                right -= 1
                if height[right] < height[right + 1]:
                    continue
            max_water = max(max_water, min(height[right], height[left]) * (right - left))
        return max_water

sol = Solution()
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height1))

