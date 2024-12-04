# 42. 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        ans = 0
        stack = []
        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                top = stack.pop()
                if not stack:
                    break

                left = stack[-1]
                wid = i - left - 1
                h = min(height[i], height[left]) - height[top]
                ans += wid * h
            stack.append(i)

        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))  # Output: 6
