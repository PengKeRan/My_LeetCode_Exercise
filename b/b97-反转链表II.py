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
        cnt = 1
        res = head
        while head:
            if cnt < left or cnt > right:
                cnt += 1
                head = head.next
                continue
            else:
                cur = head
                prev = None
                while cur:
                    if cnt == right:
                        break
                    temp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = temp
                    cnt += 1
                prev.next = cur
                return res
        return None
