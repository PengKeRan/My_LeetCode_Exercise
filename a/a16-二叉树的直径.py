"""
543. 二叉树的直径
给你一棵二叉树的根节点，返回该树的 直径 。
二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
两节点之间路径的 长度 由它们之间边数表示。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left) + 1, self.height(root.right) + 1)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        max_l = self.height(root.left) + self.height(root.right)
        max_l = max(max_l, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max_l

sol = Solution()
root1 = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4, left=None, right=None),
                                      right=TreeNode(val=5, left=None, right=None)),
                 right=TreeNode(val=3, left=None, right=None))
print(sol.diameterOfBinaryTree(root1))
