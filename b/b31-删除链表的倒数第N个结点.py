"""
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res = ListNode()
        if head.next is None:
            return None
        pos = 1
        length = 1
        temp = head
        while temp.next is not None:
            length += 1
            temp = temp.next
        n = length - n + 1
        temp_h = head
        temp_r = res
        while temp_h is not None:
            if pos == n:
                temp_h = temp_h.next
                pos += 1
                continue
            temp_r.next = ListNode(val=temp_h.val)
            temp_r = temp_r.next
            temp_h = temp_h.next
            pos += 1
        return res.next



head1 = ListNode(val=1,
                 next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))
n1 = 2
head2 = ListNode(val=1, next=None)
n2 = 1
head3 = ListNode(val=1, next=ListNode(val=2, next=None))
n3 = 1
sol = Solution()
print(sol.removeNthFromEnd(head1, n1))
# print(sol.removeNthFromEnd(head2, n2))
# print(sol.removeNthFromEnd(head3, n3))
