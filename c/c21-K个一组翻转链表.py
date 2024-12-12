# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head

        prev = dummy

        while prev:
            node_cnt = prev
            for _ in range(k):
                node_cnt = node_cnt.next
                if node_cnt is None:
                    return dummy.next

            cur = prev.next
            for _ in range(k - 1):
                next = cur.next
                cur.next = next.next
                next.next = prev.next
                prev.next = next

            prev = cur

        return dummy.next
