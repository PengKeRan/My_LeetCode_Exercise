"""
1941. 检查是否所有字符出现次数相同
给你一个字符串s，如果s是一个好字符串，请你返回true，否则请返回false。
如果s中出现过的所有字符的出现次数相同，那么我们称字符串s是好字符串。
"""


def areOccurrencesEqual(s):
    """
    :type s: str
    :rtype: bool
    """
    if not len(s):
        return True
    time = s.count(s[0])
    for word in s:
        if not time == s.count(word):
            return False
        time = s.count(word)
    return True

print(areOccurrencesEqual('abacbc'))
print(areOccurrencesEqual('aaabb'))
