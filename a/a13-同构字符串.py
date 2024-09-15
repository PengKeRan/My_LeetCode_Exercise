"""
205.同构字符串
给定两个字符串s和t，判断它们是否是同构的。
如果s中的字符可以按某种映射关系替换得到t，那么这两个字符串是同构的。
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool22
        """
        # 双映射
        if len(s) != len(t):
            return False
        s_table = dict()
        t_table = dict()
        for i in range(len(s)):
            if s[i] not in s_table.keys():
                s_table[s[i]] = t[i]
            if t[i] not in t_table.keys():
                t_table[t[i]] = s[i]
            if t[i] != s_table[s[i]] or s[i] != t_table[t[i]]:
                return False
        return True


        # if len(s) != len(t):
        #     return False
        # if len(s) == 1:
        #     return True
        # s_res = -2
        # t_res = -2
        # for i in range(1, len(s)):
        #     if s[i] in s[0:i]:
        #         for j in range(0, i):
        #             if s[j] == s[i]:
        #                 break
        #         s_res=j
        #     else:
        #         s_res=-1
        #     if t[i] in t[0:i]:
        #         for j in range(0, i):
        #             if t[j] == t[i]:
        #                 break
        #         t_res=j
        #     else:
        #         t_res=-1
        #     if s_res != t_res:
        #         return False
        # return True


sol = Solution()
s = "egg12"
t = "add22"
print(sol.isIsomorphic(s, t))
