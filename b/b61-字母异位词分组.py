# 49. 字母异位词分组
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def check(str, _dict):
            if len(str) != len(_dict):
                return False
            word_dict = list(_dict)
            for i in range(len(str)):
                if str[i] not in word_dict:
                    return False
                else:
                    word_dict.remove(str[i])
            return True

        word_dict_list = []
        res = []
        flag = False
        for str in strs:
            for i in range(len(word_dict_list)):
                word_dict = word_dict_list[i]
                flag = check(str, word_dict)
                if flag:
                    res[i].append(str)
                    break
            if not flag:
                res.append([str])
                temp = [ch for ch in str]
                word_dict_list.append(temp)
        return res


sol = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = ["a"]
print(sol.groupAnagrams(strs))
