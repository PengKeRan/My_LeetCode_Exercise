# 76. 最小覆盖子串
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
# 如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        tar_counter = Counter(t)
        window_counter = Counter()

        required = len(tar_counter)  # 所需字符种类
        formed = 0  # 当前满足的字符种类

        res = ""
        left = 0
        right = 0

        while right < n:
            if s[right] in tar_counter:
                window_counter[s[right]] += 1
                if window_counter[s[right]] == tar_counter[s[right]]:
                    formed += 1

            while left <= right and formed == required:
                if not res or len(res) > right - left + 1:
                    res = s[left : right + 1]

                if s[left] in tar_counter:
                    if window_counter[s[left]] == tar_counter[s[left]]:
                        formed -= 1
                    window_counter[s[left]] -= 1
                left += 1
            right += 1
        return res


s = "AABC"
t = "ABC"
sol = Solution()
print(sol.minWindow(s, t))
