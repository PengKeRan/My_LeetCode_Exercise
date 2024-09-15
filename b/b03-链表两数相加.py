"""
2. 两数相加
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0开头。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    arr = ListNode(0)
    node = arr
    plus_one = 0
    while l1 and l2:
        node.next = ListNode((l1.val + l2.val + plus_one) % 10)
        plus_one = (l1.val + l2.val + plus_one) // 10

        l1 = l1.next
        l2 = l2.next
        node = node.next

    if l1:
        while l1:
            node.next = ListNode((l1.val + plus_one) % 10)
            plus_one = (l1.val + plus_one) // 10
            node = node.next
            l1 = l1.next

    if l2:
        while l2:
            node.next = ListNode((l2.val + plus_one) % 10)
            plus_one = (l2.val + plus_one) // 10
            node = node.next
            l2 = l2.next

    if plus_one == 1:
        node.next = ListNode(1)

    return arr.next


print(addTwoNumbers([6, 5], [6]))
