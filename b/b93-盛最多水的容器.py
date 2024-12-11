# 11. 盛最多水的容器
# 提示
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器。


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        leftH = -1
        rightH = -1
        left = 0
        right = n - 1
        ans = -1
        while left < n and right >= 0 and left < right:
            if height[left] > leftH:
                leftH = height[left]
                ans = max(ans, (right - left) * min(height[left], height[right]))

            if height[right] > rightH:
                rightH = height[right]
                ans = max(ans, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height))
