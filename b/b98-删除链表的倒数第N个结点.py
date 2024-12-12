# 19. 删除链表的倒数第 N 个结点
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # 两次遍历
        # sz = 0
        # temp = head
        # while temp:
        #     sz += 1
        #     temp = temp.next

        # cnt = 0
        # dummy = ListNode()
        # dummy.next = head
        # prev = dummy
        # while True:
        #     cnt += 1
        #     cur = prev.next
        #     if cnt == sz - n + 1:
        #         prev.next = cur.next
        #         cur.next = None
        #         return dummy.next
        #     prev = prev.next

        # 单次遍历
        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = dummy
        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
