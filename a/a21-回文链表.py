# 234.回文链表
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # arr = []
        # while head:
        #     arr.append(head.val)
        #     head = head.next
        # s = 0
        # e = len(arr)-1
        # while s < e:
        #     if arr[s] != arr[e]:
        #         return False
        #     s += 1
        #     e -= 1
        # return True
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        pre = head
        prepre = None
        while fast is not None and fast.next is not None:
            pre = slow
            slow = slow.next
            fast = fast.next.next
            pre.next = prepre
            prepre = pre

        if fast is not None:
            slow = slow.next

        while slow is not None and pre is not None:
            if slow.val != pre.val:
                return False
            slow = slow.next
            pre = pre.next

        return True


sol = Solution()
head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=2, next=ListNode(val=1, next=None))))

print(sol.isPalindrome(head))
