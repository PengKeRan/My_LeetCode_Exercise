# 155. 最小栈
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minNum = -1

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.stack:
            diff = val - self.minNum
            self.stack.append(diff)
            self.minNum = self.minNum if diff > 0 else val
        else:
            self.stack.append(0)
            self.minNum = val

    def pop(self):
        """
        :rtype: None
        """
        diff = self.stack.pop()
        if diff > 0:
            top = self.minNum + diff
        else:
            top = self.minNum
            self.minNum = self.minNum - diff
        return top

    def top(self):
        """
        :rtype: int
        """
        return self.minNum + self.stack[-1] if self.stack[-1] > 0 else self.minNum

    def getMin(self):
        """
        :rtype: int
        """
        return self.minNum


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(4)
obj.push(3)
obj.push(5)
obj.push(1)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
