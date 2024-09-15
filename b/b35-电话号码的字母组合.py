"""
17.电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
2=abc
3=def
4=ghi
5=jkl
6=mno
7=pqrs
8=tuv
9=wxyz
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        arr = []
        for i in range(4):
            if i >= len(digits):
                arr.append([''])
                continue
            if digits[i] == '2':
                arr.append(['a', 'b', 'c'])
            if digits[i] == '3':
                arr.append(['d', 'e', 'f'])
            if digits[i] == '4':
                arr.append(['g', 'h', 'i'])
            if digits[i] == '5':
                arr.append(['j', 'k', 'l'])
            if digits[i] == '6':
                arr.append(['m', 'n', 'o'])
            if digits[i] == '7':
                arr.append(['p', 'q', 'r', 's'])
            if digits[i] == '8':
                arr.append(['t', 'u', 'v'])
            if digits[i] == '9':
                arr.append(['w', 'x', 'y', 'z'])
        final_list = []
        for i in arr[0]:
            for j in arr[1]:
                for m in arr[2]:
                    for n in arr[3]:
                        final_list.append(i+j+m+n)
        return final_list


sol = Solution()
digits1 = "23"
print(sol.letterCombinations(digits1))
