# 5. 最长回文子串
# 给你一个字符串 s，找到 s 中最长的回文子串。

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def palindrome(s, left, right):
            while left>=0 and right<=len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        n = len(s)
        if n < 2:
            return s
        start, end = 0, 0
        maxLen = 0
        for i in range(n-1):
            oddStr = palindrome(s, i, i)
            evenStr = palindrome(s, i, i+1)
            maxLen = max(len(oddStr), len(evenStr))
            if maxLen > end-start+1:
                if maxLen % 2 == 0:
                    start = i - (maxLen // 2) + 1
                    end = i + (maxLen // 2)
                else: 
                    start = i - (maxLen // 2)
                    end = i + (maxLen // 2)
        return s[start:end+1]
        

sol = Solution()
s = "bb"
# s = "cbbd"
print(sol.longestPalindrome(s))