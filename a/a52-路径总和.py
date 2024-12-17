# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        newT = targetSum - root.val
        return (
            (newT == 0 and not root.left and not root.right)
            or self.hasPathSum(root.left, newT)
            or self.hasPathSum(root.right, newT)
        )
