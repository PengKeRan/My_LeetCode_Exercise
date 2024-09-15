"""
66. 加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位，数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    arr = [0 for i in range(len(digits))]
    carry = 0
    arr[len(digits) - 1] = (digits[len(digits) - 1] + 1) % 10
    carry = (digits[len(digits) - 1] + 1) // 10
    for i in range(len(digits) - 2, -1, -1):
        if carry == 1:
            arr[i] = (digits[i] + 1) % 10
            carry = (digits[i] + 1) // 10
        else:
            arr[i] = digits[i]
            carry = 0

    if carry == 1:
        arr.insert(0, 1)
    return arr


print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([0]))
print(plusOne([9, 9, 9]))
