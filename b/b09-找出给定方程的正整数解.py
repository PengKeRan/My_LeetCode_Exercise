"""
1237. 找出给定方程的正整数解
给你一个函数f(x, y)和一个目标结果z，函数公式未知，请你计算方程f(x,y) == z所有可能的正整数 数对x 和 y。满足条件的结果数对可以按任意顺序返回。
尽管函数的具体式子未知，但它是单调递增函数，也就是说：
f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)
"""

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""


class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        arr = []
        for x in range(1, 1000):
            for y in range(1, 1000):
                if customfunction.f(x, y) == z:
                    arr.append([x, y])
                if customfunction.f(x, y) > z:
                    break
        return arr