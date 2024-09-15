"""
646. 最长数对链
给你一个由n个数对组成的数对数组pairs，其中pairs[i] = [lefti, righti]且lefti< righti 。
现在，我们定义一种 跟随 关系，当且仅当b < c时，数对p2 = [c, d]才可以跟在p1 = [a, b]后面。我们用这种形式来构造 数对链 。
找出并返回能够形成的 最长数对链的长度 。
你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。
"""


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # 1.贪心
        num = 1
        pairs = sorted(pairs, key=lambda x: x[1])
        temp = pairs[0][1]
        for i in range(1,len(pairs)):
            if temp < pairs[i][0]:
                temp = pairs[i][1]
                num += 1
        return num

        # 2.动态规划
        # arr = [1] * len(pairs)
        # pairs = sorted(pairs, key=lambda x: x[0])
        # for i in range(len(pairs)):
        #     for j in range(i):
        #         if pairs[i][0] > pairs[j][1]:
        #             arr[i] = max(arr[i], arr[j] + 1)
        # return max(arr)


pairs1 = [[1, 2], [2, 3], [3, 4]]
pairs2 = [[1, 2], [7, 8], [4, 5]]
sol = Solution()
print(sol.findLongestChain(pairs1))  # 2
print(sol.findLongestChain(pairs2))  # 3
