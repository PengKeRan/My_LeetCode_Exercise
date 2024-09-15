"""
114. 二叉树展开为链表
给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 方法一：寻找前驱节点
        while root is not None:
            if root.left is not None:
                lr = root.left
                while lr.right is not None:
                    lr = lr.right
                lr.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        # 方法二：先先序遍历，再重组树
        # arr = []
        #
        # def preOrder(root):
        #     if root is not None:
        #         arr.append(root)
        #         preOrder(root.left)
        #         preOrder(root.right)
        #
        # preOrder(root)
        #
        # for i in range(1, len(arr)):
        #     prev, curr = arr[i - 1], arr[i]
        #     prev.left = None
        #     prev.right = curr


root1 = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None),
                                      right=TreeNode(val=4, left=None, right=None)),
                 right=TreeNode(val=5, left=None, right=TreeNode(val=6, left=None, right=None)))

sol = Solution()
print(sol.flatten(root1))
