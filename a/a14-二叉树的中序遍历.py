"""
94. 二叉树的中序遍历
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        def middle(root):
            nonlocal arr
            if root is None:
                return
            if root.left is not None:
                middle(root.left)
            arr.append(root.val)
            if root.right is not None:
                middle(root.right)
            return
        middle(root)
        return arr



root1 = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=None))
sol = Solution()
print(sol.inorderTraversal(root1))
