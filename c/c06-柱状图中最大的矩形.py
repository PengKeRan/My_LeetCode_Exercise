# 84. 柱状图中最大的矩形
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # O(N^2)
        # n = len(heights)
        # max_s = 0
        # for i in range(n):
        #     left = 0
        #     right = 0
        #     while i-left >= 0 and heights[i-left] >= heights[i]:
        #         left += 1
        #     while i+right <= n-1 and heights[i+right] >= heights[i]:
        #         right += 1
        #     max_s = max(max_s, heights[i] * (right+left-1))
        # return max_s

        # 单调栈
        # n = len(heights)
        # if n == 0:
        #     return 0
        # left_res = [-1 for _ in range(n)]
        # stack = []
        # for i in range(n):
        #     while stack and heights[stack[-1]] >= heights[i]:
        #         stack.pop()
        #     if stack:
        #         left_res[i] = stack[-1]
        #     else:
        #         left_res[i] = -1
        #     stack.append(i)
        #
        # right_res = [n for _ in range(n)]
        # stack = []
        # for i in range(n - 1, -1, -1):
        #     while stack and heights[stack[-1]] >= heights[i]:
        #         stack.pop()
        #     if stack:
        #         right_res[i] = stack[-1]
        #     else:
        #         right_res[i] = n
        #     stack.append(i)
        #
        # res = [heights[i]*(right_res[i]-left_res[i]-1) for i in range(n)]
        # return max(res)

        # 单调栈，优化
        n = len(heights)
        if n == 0:
            return 0
        left_res = [-1 for _ in range(n)]
        right_res = [n for _ in range(n)]
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right_res[stack[-1]] = i
                stack.pop()
            if stack:
                left_res[i] = stack[-1]
            else:
                left_res[i] = -1
            stack.append(i)

        res = [heights[i] * (right_res[i] - left_res[i] - 1) for i in range(n)]
        return max(res)


sol = Solution()
heights1 = [6, 7, 5, 2, 4, 5, 9, 3]
heights2 = [2, 4]
print(sol.largestRectangleArea(heights1))
