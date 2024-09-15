"""
1763. 最长的美好子字符串
当一个字符串 s包含的每一种字母的大写和小写形式 同时出现在 s中，就称这个字符串s是 美好 字符串。比方说，"abABB"是美好字符串，因为'A' 和'a'
同时出现了，且'B' 和'b'也同时出现了。然而，"abA"不是美好字符串因为'b'出现了，而'B'没有出现。
给你一个字符串s，请你返回s最长的美好子字符串。如果有多个答案，请你返回最早出现的一个。如果不存在美好子字符串，请你返回一个空字符串。
"""

import re


def longestNiceSubstring(s):
    start = 0
    end = 0
    beautiful = False
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            if i == j or j - i == 1:
                continue
            print("开始判断是否完美")
            print(f"子串:{s[i:j]} 长度：i:{i},j:{j}")
            # 判断子串是否完美
            for k in range(len(s[i:j])):
                if 65 <= ord(s[i:j][k]) <= 90:
                    print(f"为{s[i:j][k]}找{chr(ord(s[i:j][k]) + 32)}：{re.findall(chr(ord(s[i:j][k]) + 32), s[i:j])}")
                    if len(re.findall(chr(ord(s[i:j][k]) + 32), s[i:j])) > 0:
                        beautiful = True
                    else:
                        beautiful = False
                        break
                elif 97 <= ord(s[i:j][k]) <= 122:
                    print(f"为{s[i:j][k]}找{chr(ord(s[i:j][k]) - 32)}：{re.findall(chr(ord(s[i:j][k]) - 32), s[i:j])}")
                    if len(re.findall(chr(ord(s[i:j][k]) - 32), s[i:j])) > 0:
                        beautiful = True
                    else:
                        beautiful = False
                        break
                else:
                    return ""

            # 判断子串与已有完美串位置关系
            if beautiful and (j - i) > (end - start):
                # print(f'替换完美子串：从{start},{end}--{s[start:end]}替换为{i},{j}--{s[i:j]}')
                start = i
                end = j
            else:
                beautiful = False
                continue
    # 如果存在，返回字符串；不存在返回""
    return s[start:end]


print(longestNiceSubstring('VvaNEne'))

# a='a'
# b=56
# print( a + " 的ASCII 码为", ord(a))
# print( b , " 对应的字符为", chr(b))
