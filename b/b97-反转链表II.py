# 92. 反转链表 II
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
# 请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        dummy.next = head
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return dummy.next
