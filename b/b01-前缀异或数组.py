"""
2433. 找出前缀异或的原始数组
给你一个长度为 n 的 整数 数组 pref 。找出并返回满足下述条件且长度为 n 的数组 arr ：
pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
注意 ^ 表示 按位异或（bitwise-xor）运算。
可以证明答案是 唯一 的。
"""


def findArray(pref):
    """
    :type pref: List[int]
    :rtype: List[int]
    """
    arr = [0 for i in range(len(pref))]
    arr[0] = pref[0]
    if len(pref) == 1:
        return arr
    for i in range(1, len(pref)):
        # print(f"arr[{i}]={pref[i - 1]}^{pref[i]}")
        arr[i] = pref[i - 1] ^ pref[i]

    return arr


print(findArray([5, 2, 0, 3, 1]))
