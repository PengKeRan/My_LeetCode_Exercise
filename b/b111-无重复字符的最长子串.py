# 3. 无重复字符的最长子串
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left = 0
        right = 0
        memo = {}
        res = 0
        while right < n:
            if s[right] not in memo.keys():
                memo[s[right]] = 1
                right += 1
                res = max(res, right - left)
                continue
            if memo[s[right]] == 1:
                res = max(res, right - left)
                while True:
                    if s[left] == s[right]:
                        memo.pop(s[right])
                        left += 1
                        break
                    memo.pop(s[left])
                    left += 1
        return res


s = "abba"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
