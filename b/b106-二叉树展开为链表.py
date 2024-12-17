# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        rootR = root.right

        target = root
        root.right = self.flatten(root.left)
        while target.right:
            target = target.right

        root.left = None

        target.right = self.flatten(rootR)

        return root
