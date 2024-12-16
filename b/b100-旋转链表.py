# 61. 旋转链表
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        total = 1
        cur = head
        while cur.next:
            cur = cur.next
            total += 1

        cur.next = head

        for _ in range((total - k % total)):
            cur = cur.next

        res = cur.next
        cur.next = None
        return res

    #     if head is None:
    #         return head

    #     total = 0
    #     cur = head
    #     while cur:
    #         total += 1
    #         cur = cur.next
    #     k = k % total
    #     head = self.reverse_range(head, 0, total)
    #     head = self.reverse_range(head, 0, k)
    #     head = self.reverse_range(head, k, total)
    #     return head

    # def reverse_range(self, head, s, e):
    #     dummy = ListNode()
    #     dummy.next = head
    #     prev = dummy

    #     for _ in range(s):
    #         prev = prev.next

    #     cur = prev.next
    #     for _ in range(e - s - 1):
    #         next = cur.next
    #         cur.next = next.next
    #         next.next = prev.next
    #         prev.next = next
    #     return dummy.next
