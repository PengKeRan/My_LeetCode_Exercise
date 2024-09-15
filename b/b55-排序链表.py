# 148. 排序链表
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # def printList(node):
        #     while node is not None:
        #         print(node.val, end="-")
        #         node = node.next
        #     print('\n')
        #     return

        def split(h):
            slow = h
            fast = h
            while fast is not None and fast.next is not None:
                pre = slow
                slow = slow.next
                fast = fast.next
                fast = fast.next
            pre.next = None
            return h, slow

        def merge(h1, h2):
            temp = ListNode(val=None, next=None)
            hh = temp
            while h1 and h2:
                if h1.val <= h2.val:
                    temp.next = ListNode(val=h1.val, next=None)
                    h1 = h1.next
                else:
                    temp.next = ListNode(val=h2.val, next=None)
                    h2 = h2.next
                temp = temp.next
            if h1:
                temp.next = h1
            if h2:
                temp.next = h2
            return hh.next

        def sort(h):
            if h is None or h.next is None:
                return h
            left_part, right_part = split(h)
            left_part =sort(left_part)
            right_part =sort(right_part)
            res = merge(left_part,right_part)
            return res



        # left_part, right_part = split(head)
        # print("left_part:", end='')
        # printList(left_part)
        # print("right_part:", end='')
        # printList(right_part)
        #
        # merged_list = merge(left_part, right_part)
        # print("merged_list:", end='')
        # printList(merged_list)

        # res = sort(head)
        # printList(res)
        return sort(head)





sol = Solution()
head = ListNode(val=4, next=ListNode(val=2, next=ListNode(val=1, next=ListNode(val=3, next=None))))
print(sol.sortList(head))
