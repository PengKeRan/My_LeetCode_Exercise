# 438. 找到字符串中所有字母异位词
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_dict = [word for word in p]
        window = len(p)
        word_dict = list(p_dict)
        extra_dict = []
        res = []
        if window > len(s):
            return res
        for i in range(window):
            if s[i] in p_dict:
                if s[i] in word_dict:
                    word_dict.remove(s[i])
                else:
                    extra_dict.append(s[i])
            else:
                extra_dict.append(s[i])
        if not extra_dict and not word_dict:
            res.append(0)

        for i in range(window, len(s)):
            # s[i-window]
            if s[i-window] not in p_dict:
                extra_dict.remove(s[i-window])
            else:
                if s[i-window] in extra_dict:
                    extra_dict.remove(s[i-window])
                else:
                    word_dict.append(s[i-window])
            # s[i]
            if s[i] not in p_dict:
                extra_dict.append(s[i])
            else:
                if s[i] in word_dict:
                    word_dict.remove(s[i])
                else:
                    extra_dict.append(s[i])
            # check
            if not extra_dict and not word_dict:
                res.append(i-window+1)

        return res




sol = Solution()
s = "aaaaaaaaaa"
p = "aaaaaaaaaaaaaa"
print(sol.findAnagrams(s, p))
