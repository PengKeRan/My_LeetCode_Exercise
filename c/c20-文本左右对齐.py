# 68. 文本左右对齐
# 给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
# 你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
# 注意:
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        n = len(words)
        group = []
        temp_len = 0
        res = []
        for i in range(n):
            word_len = len(words[i])
            if temp_len + word_len + len(group) > maxWidth:
                res.append(self.fillALine(group, temp_len, maxWidth))

                group = [words[i]]
                temp_len = word_len
            else:
                group.append(words[i])
                temp_len += word_len
        if group:
            temp_arr = ""
            for i in range(len(group)):
                temp_arr += group[i]
                if len(temp_arr) < maxWidth:
                    temp_arr += " "
            temp_arr += (maxWidth - len(temp_arr)) * " "

            res.append(temp_arr)

        return res

    def fillALine(self, group, temp_len, maxWidth):
        if len(group) == 1:
            return group[0] + " " * (maxWidth - temp_len)
        space_len = maxWidth - temp_len
        min_space = space_len // (len(group) - 1)
        extra_space = space_len % (len(group) - 1)
        temp_arr = ""
        for i in range(len(group) - 1):
            temp_arr += group[i]
            temp_arr += " " * min_space
            if extra_space > 0:
                temp_arr += " "
                extra_space -= 1

        temp_arr += group[-1]
        return temp_arr


sol = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(sol.fullJustify(words, maxWidth))
