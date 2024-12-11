# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        head = res
        flow = 0
        while l1 and l2:
            total = l1.val + l2.val + flow
            temp_val = total % 10
            flow = 1 if total >= 10 else 0
            head.next = ListNode(val=temp_val)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                total = l1.val + flow
                temp_val = total % 10
                flow = 1 if total >= 10 else 0
                head.next = ListNode(val=temp_val)
                head = head.next
                l1 = l1.next
        if l2:
            while l2:
                total = l2.val + flow
                temp_val = total % 10
                flow = 1 if total >= 10 else 0
                head.next = ListNode(val=temp_val)
                head = head.next
                l2 = l2.next
        if flow:
            head.next = ListNode(val=1)

        return res.next
