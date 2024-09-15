"""
155.最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:
MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。
"""


class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack = self.stack[0:(len(self.stack) - 1)]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
