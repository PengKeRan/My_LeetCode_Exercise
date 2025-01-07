# 206. 反转链表
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        cur = prev.next
        while True:
            if cur is None or cur.next is None:
                return dummy.next
            next = cur.next
            cur.next = next.next
            next.next = prev.next
            prev.next = next

        # def printList(node):
        #     while node is not None:
        #         print(node.val)
        #         node = node.next
        #     return
        # # if head is None or head.next is None:
        # #     return head
        # cur = head
        # pre = None
        # while cur:
        #     temp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = temp
        # # printList(pre)
        # return pre
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        cur = pre.next
        while True:
            if cur is None or cur.next is None:
                return dummy.next
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next


sol = Solution()
head = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None))),
    ),
)
print(sol.reverseList(head))
