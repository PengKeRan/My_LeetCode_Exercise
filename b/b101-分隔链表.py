# 86. 分隔链表
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
# 你应当 保留 两个分区中每个节点的初始相对位置。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        # dummy = ListNode()
        # dummy.next = head
        # prev = dummy
        # cur = head
        # last_small = dummy
        # while cur:
        #     if cur.val < x:
        #         if last_small.next == cur:
        #             last_small = cur
        #             prev = prev.next
        #             cur = cur.next
        #             continue
        #         next = cur.next
        #         prev.next = next
        #         cur.next = last_small.next
        #         last_small.next = cur
        #         last_small = last_small.next
        #         cur = prev.next
        #     else:
        #         prev = prev.next
        #         cur = cur.next
        # return dummy.next

        small_head = ListNode()
        large_head = ListNode()

        small_dummy = small_head
        large_dummy = large_head

        while head:
            if head.val < x:
                small_dummy.next = head
                small_dummy = small_dummy.next
            else:
                large_dummy.next = head
                large_dummy = large_dummy.next
            head = head.next

        small_dummy.next = large_head.next
        large_dummy.next = None

        return small_dummy.next
