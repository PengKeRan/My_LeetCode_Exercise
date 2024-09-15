"""
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    num = 0
    i = 0
    j = 1
    flag = False
    if len(s) == 1:
        return 1
    while i < len(s) - 1:
        while j < len(s):
            # print(s[i:j])
            # j处的字符出现重复
            if s[i:j].count(s[j]) >= 1:
                # print(f"{num}替换为{j - i}({j}-{i})")
                num = max(num, j - i)
                flag = True
                i = s[i:j].index(s[j])+i+1
                j = i + 1
                break
            else:
                num = max(num, j - i+1)
                flag = False
                j += 1
        if not flag:
            i += 1
            flag = False
    return num

    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     if len(s) <= 1:
    #         return len(s)
    #     max_l = 1
    #     single_str = ''
    #     for i in range(0, len(s)):
    #         if s[i] in single_str:
    #             single_str = single_str[single_str.index(s[i])+1:]
    #         single_str += s[i]
    #         if len(single_str) > max_l:
    #             max_l = len(single_str)
    #     return max_l

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("dvdf"))
