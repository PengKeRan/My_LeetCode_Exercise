# 49. 字母异位词分组


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        memo = dict()
        for s in strs:
            counts = [0 for _ in range(26)]
            for ch in s:
                counts[ord(ch) - ord("a")] += 1
            if tuple(counts) in memo.keys():
                memo[tuple(counts)].append(s)
            else:
                memo[tuple(counts)] = [s]
        return memo.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(strs))
