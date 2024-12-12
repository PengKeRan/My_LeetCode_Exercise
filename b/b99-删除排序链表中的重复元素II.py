# 82. 删除排序链表中的重复元素 II
# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        cur = prev.next
        while cur:
            flag = False
            while cur.next and cur.val == cur.next.val:
                flag = True
                cur = cur.next

            if flag:
                prev.next = cur.next
            else:
                prev = prev.next

            cur = cur.next
        return dummy.next
