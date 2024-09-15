"""
101. 对称二叉树
给你一个二叉树的根节点 root ， 检查它是否轴对称。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.symmetrical(root.left, root.right)

    def symmetrical(self, left, right):
        if left is not None and right is not None:
            if left.val != right.val:
                return False
            else:
                return self.symmetrical(left.left, right.right) and self.symmetrical(left.right, right.left)
        if left is None and right is None:
            return True
        return False
