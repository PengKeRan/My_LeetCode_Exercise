# 224. 基本计算器
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        while i < len(s):
            if s[i] == "-":
                pos = i - 1
                while pos >= 0 and s[pos] == " " and not s[pos].isdigit():
                    pos -= 1
                if pos >= 0 and (s[pos].isdigit() or s[pos] == ")"):
                    i += 1
                    continue
                if pos < 0 or s[pos] in {"+", "-", "(", "*", "/"}:
                    s = s[:i] + "0" + s[i:]
                    i += 1
            i += 1
        tokens = self.getToken(s)
        return self.calTokens(tokens)

    def getToken(self, s):
        operator = []
        tokens = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == " ":
                i += 1
                continue
            elif c == "(":
                operator.append(c)
            elif c == ")":
                while operator:
                    top = operator.pop()
                    if top == "(":
                        break
                    tokens.append(top)
            elif c == "+":
                temp = []
                while operator:
                    if operator[-1] in {"+", "(", ")"}:
                        break
                    tokens.append(operator.pop())
                operator.append(c)
            elif c == "-":
                temp = []
                while operator:
                    if operator[-1] in {"+", "(", ")"}:
                        break
                    tokens.append(operator.pop())
                operator.append(c)
            elif c in {"*", "/"}:
                operator.append(c)
            else:
                start = i
                end = i
                while end < len(s) and s[end] not in {
                    "+",
                    "-",
                    "(",
                    ")",
                    "*",
                    "/",
                    " ",
                }:
                    end += 1
                tokens.append(float(s[start:end]))
                i = end - 1
            i += 1
        while operator:
            tokens.append(operator.pop())
        return tokens

    def calTokens(self, tokens):
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                stack.append(-stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                stack.append(float(int(1 / stack.pop() * stack.pop())))
            else:
                stack.append(float(c))
        return int(stack[0])


s = "(6)-(8)-(7)+(1+(6))"
sol = Solution()
print(sol.calculate(s))
