# 739. 每日温度
# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
# 其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
# 如果气温在这之后都不会升高，请在该位置用 0 来代替。

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # n = len(temperatures)
        # ans = [0 for _ in range(n)]
        # for i in range(n - 2, -1, -1):
        #     j = 1
        #     print(i)
        #     while temperatures[i + j] <= temperatures[i] and i + j < n - 1:
        #         if ans[i + j] == 0:
        #             break
        #         j = j + ans[i + j]
        #     if temperatures[i + j] > temperatures[i]:
        #         ans[i] = j
        #     else:
        #         continue
        # return ans
        n = len(temperatures)
        ans = [0 for _ in range(n)]
        stack = [0]
        for i in range(1, n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i-index

            stack.append(i)

        return ans


sol = Solution()
temperatures1 = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
temperatures2 = [34, 80, 80, 34, 34, 80, 80, 80, 80, 34]
print(sol.dailyTemperatures(temperatures1))
