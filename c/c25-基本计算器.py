# 224. 基本计算器
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        tokens = self.getToken(s)
        return tokens

    def getToken(self, s):
        operator = []
        tokens = []
        for c in s:
            if c == "(":
                operator.append(c)
            elif c == ")":
                while operator:
                    top = operator.pop()
                    if top == "(":
                        break
                    tokens.append(top)
            elif c in {"+", "-"}:
                temp = []
                while operator:
                    if operator[-1] in {"+", "-"}:
                        break
                    temp.append(operator.pop())
                operator.append(c)
                while temp:
                    operator.append(temp.pop())
            elif c in {"*", "/"}:
                operator.append(c)
            else:
                tokens.append(float(c))
        while operator:
            tokens.append(operator.pop())
        return tokens

    def calTokens(self, tokens):
        for c in tokens:
            if c ==
        return 0


s = "(1+(4+5+2)-3)+(6+8)"
sol = Solution()
print(sol.calculate(s))
