"""
20.有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        if len(s) % 2 == 1:
            return False
        arr = []
        for ch in s:
            if len(arr) == 0:
                arr.append(ch)
            elif ch == ')' and arr[-1] == '(':
                arr = arr[0:len(arr) - 1]
            elif ch == ']' and arr[-1] == '[':
                arr = arr[0:len(arr) - 1]
            elif ch == '}' and arr[-1] == '{':
                arr = arr[0:len(arr) - 1]
            else:
                arr.append(ch)
        return True if len(arr) == 0 else False


s1 = "()"
s2 = "()[]{}"
s3 = "){"
sol = Solution()
# print(sol.isValid(s1))  # T
# print(sol.isValid(s2))  # T
print(sol.isValid(s3))  # F
