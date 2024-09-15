"""
剑指 Offer II 083. 没有重复元素集合的全排列
给定一个不含重复数字的整数数组nums，返回其所有可能的全排列。可以按任意顺序返回答案。
"""


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) == 1:
        return [nums]

    def orders(arr):
        ls = []
        # print(f"arr:{arr}")
        if len(arr) == 1:
            ls.append([arr[0]])
            return ls
        for i in range(len(arr)):
            # print(f"i:{i}")
            tempArr = list(arr)
            tempArr.remove(arr[i])
            for order in orders(tempArr):
                ls.append(sum([[arr[i]], order], []))
                # ls.append(sum([order, [arr[i]]], []))
        return ls

    return orders(nums)


print(permute([1]))
print(permute([1, 2, 3]))
