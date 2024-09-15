# 226. 翻转二叉树
# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root



root1 = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1, left=None, right=None),
                                      right=TreeNode(val=3, left=None, right=None)),
                 right=TreeNode(val=7, left=TreeNode(val=6, left=None, right=None),
                                right=TreeNode(val=9, left=None, right=None)))
