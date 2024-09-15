"""
21.合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 1.递归
        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1
        # if list1.val < list2.val:
        #     list1.next = self.mergeTwoLists(self, list1.next, list2)
        # elif list1.val > list2.val:
        #     list2.next = self.mergeTwoLists(self, list1, list2.next)

        # 2.
        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1
        # node1 = list1
        # node2 = list2
        # resList = None
        # while node1 is not None and node2 is not None:
        #     tempNode = ListNode()
        #     if node1.val <= node2.val:
        #         tempNode.val = node1.val
        #         tempNode.next = resList
        #         node1 = node1.next
        #     elif node2.val < node1.val:
        #         tempNode.val = node2.val
        #         tempNode.next = resList
        #         node2 = node2.next
        #     resList = tempNode
        # if node1 is not None:
        #     while node1 is not None:
        #         tempNode = ListNode()
        #         tempNode.val = node1.val
        #         tempNode.next = resList
        #         resList = tempNode
        #         node1 = node1.next
        # if node2 is not None:
        #     while node2 is not None:
        #         tempNode = ListNode()
        #         tempNode.val = node2.val
        #         tempNode.next = resList
        #         resList = tempNode
        #         node2 = node2.next
        #
        # resList = None
        # while tempNode is not None:
        #     temp = ListNode()
        #     temp.val = tempNode.val
        #     temp.next = resList
        #     resList = temp
        #     tempNode = tempNode.next
        #
        # # 将reslist反序
        # return resList

        # 3.
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        node1 = list1
        node2 = list2
        tempNode = ListNode(val=0, next=None)
        resList = tempNode
        while node1 is not None and node2 is not None:
            if node1.val <= node2.val:
                tempNode.next = ListNode(val=node1.val, next=None)
                tempNode = tempNode.next
                node1 = node1.next
            elif node2.val < node1.val:
                tempNode.next = ListNode(val=node2.val, next=None)
                tempNode = tempNode.next
                node2 = node2.next

        if node1 is not None:
            tempNode.next = node1
        if node2 is not None:
            tempNode.next = node2

        return resList.next


list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))
sol = Solution()
print(sol.mergeTwoLists(list1, list2))
