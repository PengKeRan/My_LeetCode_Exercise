# 205. 同构字符串


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        memo = dict()
        for i in range(len(s)):
            sch = s[i]
            tch = t[i]
            if sch not in memo.keys() and tch not in memo.values():
                memo[sch] = tch
            else:
                if sch not in memo.keys() or memo[sch] != tch:
                    return False
        return True
