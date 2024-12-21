# 30. 串联所有单词的子串
# 给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。
#  s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。
# 例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"，
# 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
# 返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。

from collections import Counter


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or not words[0]:
            return []

        word_len = len(words[0])
        word_count = len(words)
        substring_len = word_len * word_count

        word_counter = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            right = i
            window_counter = Counter()
            while right + word_len <= len(s):
                word = s[right : right + word_len]
                if word in word_counter:
                    window_counter[word] += 1

                    while window_counter[word] > word_counter[word]:
                        window_counter[s[left : left + word_len]] -= 1
                        left += word_len
                    if right - left + word_len == substring_len:
                        result.append(left)
                    right += word_len
                else:
                    window_counter.clear()
                    right += word_len
                    left = right
        return result


s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "good"]
sol = Solution()
print(sol.findSubstring(s, words))
