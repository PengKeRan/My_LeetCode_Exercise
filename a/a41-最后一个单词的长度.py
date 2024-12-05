class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ans = 0
        # for i in reversed(range(len(s))):
        #     if ans == 0 and s[i] == " ":
        #         continue
        #     elif s[i] == " ":
        #         return ans
        #     else:
        #         ans += 1
        # return ans
        return len(s.strip().split(" ")[-1])


print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
