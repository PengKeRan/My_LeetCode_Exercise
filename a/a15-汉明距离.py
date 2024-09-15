"""
461.汉明距离
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
给你两个整数 x 和 y，计算并返回它们之间的汉明距离。
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        arr_x = list(bin(x))
        arr_y = list(bin(y))
        arr_x = arr_x[2:len(arr_x)]
        arr_y = arr_y[2:len(arr_y)]
        length = abs(len(arr_x) - len(arr_y))
        if len(arr_x) < len(arr_y):
            for i in range(length):
                arr_x.insert(0, '0')
        if len(arr_x) > len(arr_y):
            for i in range(length):
                arr_y.insert(0, '0')
        dis = 0
        for i in range(len(arr_x)):
            if arr_x[i] != arr_y[i]:
                dis += 1
        return dis


x1 = 1
y1 = 4
x2 = 3
y2 = 1
sol = Solution()
print(sol.hammingDistance(x1, y1))
# print(sol.hammingDistance(x2,y2))
