# 125. 验证回文串
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
# 字母和数字都属于字母数字字符。
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        left = 0
        right = n - 1
        while left < n and right >= 0 and left < right:
            while left < n and not (str(s[left]).isalpha() or str(s[left]).isdigit()):
                left += 1
            while right >= 0 and not (
                str(s[right]).isalpha() or str(s[right]).isdigit()
            ):
                right -= 1
            if left >= right:
                return True
            if str(s[left]).lower() != str(s[right]).lower():
                return False
            left += 1
            right -= 1
        return True


sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))
