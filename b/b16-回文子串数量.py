"""
647. 回文子串
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
回文字符串 是正着读和倒过来读一样的字符串。
子字符串 是字符串中的由连续字符组成的一个序列。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 中心扩散法
        count = 0
        for i in range(len(s)):
            # 奇数情况
            left = i
            right = i
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            # 偶数情况
            if i == len(s) - 1:
                continue
            left = i
            right = i + 1
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count

        # # 创建子串数组，列出所有子串
        # # 创建字典，记录子串回文情况，简化遍历过程
        # son_arr = []
        # d = dict()
        # for i in range(0, len(s)):
        #     for j in range(i + 1, len(s) + 1):
        #         son_arr.append(s[i:j])
        #         d[s[i:j]] = 1 if j - i == 1 else 999
        # # 创建记录数组：记录每个子串是否回文，999-未定，0-不回文，1-回文
        # palindrome = [999 for _ in son_arr]
        # # 遍历子串数组，改变记录数字
        # for i in range(len(son_arr)):
        #     son = son_arr[i]
        #     if len(son) == 1:
        #         palindrome[i] = 1
        #         continue
        #     if d[son] == 1:
        #         palindrome[i] = 1
        #         continue
        #     for j in range(len(son) // 2):
        #         if d[son[j:(len(son) - j)]] == 1:
        #             continue
        #         if son[j] != son[len(son) - 1 - j]:
        #             palindrome[i] = 0
        #             break
        #         palindrome[i] = 1
        # # 最后计算数组的和即可
        # return sum(palindrome)


s1 = 'abc'
s2 = 'aaa'
s3 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
sol = Solution()
print(sol.countSubstrings(s1))  # 3
print(sol.countSubstrings(s2))  # 6
print(sol.countSubstrings(s3))  #
