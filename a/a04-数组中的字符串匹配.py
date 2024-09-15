"""
1408. 数组中的字符串匹配
给你一个字符串数组 words ，数组中的每个字符串都可以看作是一个单词。请你按 任意 顺序返回 words 中是其他单词的子字符串的所有单词。
如果你可以删除 words[j]最左侧和/或最右侧的若干字符得到 words[i] ，那么字符串 words[i] 就是 words[j] 的一个子字符串。
"""
import re


def stringMatching(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    arr = []
    for i in range(0, len(words)):
        num = 0
        word = words[i]
        for j in range(0, len(words)):
            if re.findall(word, words[j]):
                num += 1
        if num > 1:
            arr.append(word)
    return arr


print(stringMatching(["blue", "green", "bu"]))
