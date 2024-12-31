# 150. 逆波兰表达式求值
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
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


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
sol = Solution()
print(sol.evalRPN(tokens))
