# 20. 有效的括号
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for x in s:
            if x == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif x == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            elif x == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            else:
                stack.append(x)
        return not stack
