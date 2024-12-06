class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        n = len(s)
        i = n - 1
        left = n - 1
        right = n
        ans = ""
        while i >= 0:
            # 找到当前单词的结尾
            while i >= 0 and s[i] == " ":
                i -= 1
            if i < 0:
                break

            # 找到当前单词的开头
            end = i
            while i >= 0 and s[i] != " ":
                i -= 1
            start = i + 1

            # 添加单词到结果
            ans += s[start : end + 1] + " "
        return ans.strip()


print(Solution().reverseWords("a good   example"))
