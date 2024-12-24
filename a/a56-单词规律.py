# 290. 单词规律
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(" ")
        if len(set(pattern)) != len(set(s)) or len(pattern) != len(s):
            return False
        memo = dict()
        for i in range(len(pattern)):
            x = pattern[i]
            y = s[i]
            if x in memo.keys():
                if memo[x] != y:
                    return False
            else:
                memo[x] = y
        return True


s = "dog cat cat dog"
pattern = "abba"
print(len(pattern))
print(len(s.split(" ")))
sol = Solution()
print(sol.wordPattern(pattern, s))
