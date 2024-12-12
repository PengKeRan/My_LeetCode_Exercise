# 138. 随机链表的复制
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。
# 新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。
# 复制链表中的指针都不应指向原链表中的节点 。
# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。
# 返回复制链表的头节点。
# 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 你的代码 只 接受原链表的头节点 head 作为传入参数。
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        memo = {}
        cur = head
        while cur:
            memo[cur] = Node(x=cur.val)
            cur = cur.next
        cur = head
        while cur:
            memo[cur].next = memo.get(cur.next)
            memo[cur].random = memo.get(cur.random)
            cur = cur.next
        return memo.get(head)

        # memo = {}
        # res = Node(0)
        # node_arr = []
        # head_temp_rec = []
        # dummy = res
        # head_bp = head
        # while head:
        #     dummy.next = Node(head.val)

        #     head_temp_rec.append(head.random)
        #     memo[head] = dummy.next

        #     node_arr.append(dummy.next)
        #     dummy = dummy.next
        #     head = head.next
        # for i in range(len(head_temp_rec)):
        #     if head_temp_rec[i] is not None:
        #         node_arr[i].random = memo[head_temp_rec[i]]

        # return res.next

        dic = {}
        dummy = head
        while dummy:
            dic[dummy] = Node(dummy.val)
            dummy = dummy.next

        dummy = head
        while dummy:
            dic[dummy].next = dic.get(dummy.next)
            dic[dummy].random = dic.get(dummy.random)
            dummy = dummy.next

        return dummy[head]
