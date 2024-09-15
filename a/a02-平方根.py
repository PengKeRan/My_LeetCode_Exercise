"""
给你一个非负整数 x ，计算并返回x的 算术平方根 。
由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
注意：不允许使用任何内置指
"""


def mySqrt(x):
    if x == 1:
        return 1
    min = 0
    max = x
    while max-min > 1:
        middle = (max + min) // 2
        # print(f"min{min},max{max},middle{middle}")
        if x // middle < middle:
            max = middle
        else:
            min = middle
    return min


print(mySqrt(0))  # 0
print(mySqrt(1))  # 1
print(mySqrt(2))  # 1
print(mySqrt(3))  # 1
print(mySqrt(4))  # 2
print(mySqrt(6))  # 2
