# 160. 相交链表
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
#
# 图示两个链表在节点 c1 开始相交：

class ListNode(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A


sol = Solution()
headA = ListNode(val= 4, next= ListNode(val= 1, next= ListNode(val= 8, next= ListNode(val= 4, next= ListNode(val= 5, next= None)))))
headB = ListNode(val= 5, next= ListNode(val= 6, next= ListNode(val= 1, next= ListNode(val= 8, next= ListNode(val= 4, next= ListNode(val= 5, next= None))))))
print(sol.getIntersectionNode(headA, headB))