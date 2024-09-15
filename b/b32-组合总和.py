"""
39.组合总和
给你一个 无重复元素 的整数数组candidates 和一个目标整数target，找出candidates中可以使数字和为目标数target 的 所有不同组合 ，并以列表形式返回。
你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
对于给定的输入，保证和为target 的不同组合数少于 150 个。
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        dp = [None for _ in range(target+1)]
        dp[0] = [[]]
        for i in range(1, len(dp)):
            for candidate in candidates:
                if candidate > i:
                    break
                # dp[i] = dp[i-candidate]+candidate
                if dp[i-candidate] is None:
                    continue
                dp[i] = [] if dp[i] is None else dp[i]
                for j in range(len(dp[i-candidate])):
                    ele = dp[i-candidate][j].copy()
                    ele.append(candidate)
                    ele = sorted(ele)
                    if ele not in dp[i]:
                        dp[i].append(ele)
        if dp[-1] is None:
            return []
        return dp[-1]

candidates1 = [2, 3, 6, 7]
target1 = 7
candidates2 = [2, 3, 5]
target2 = 8
candidates3 = [2]
target3 = 1
sol = Solution()
# print(sol.combinationSum(candidates1, target1))
# print(sol.combinationSum(candidates2, target2))
print(sol.combinationSum(candidates3, target3))
