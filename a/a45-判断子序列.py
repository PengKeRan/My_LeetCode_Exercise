# 392. 判断子序列
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
# 进阶：
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                j += 1
            elif s[i] == t[j]:
                i += 1
                j += 1
            else:
                pass
        return i == len(s)


sol = Solution()
s = "abc"
t = "ahbgdc"
print(sol.isSubsequence(s, t))
