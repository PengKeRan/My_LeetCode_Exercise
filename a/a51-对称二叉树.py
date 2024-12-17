# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.check(root.left, root.right)

    def check(self, p, q):
        if p is not None and q is not None:
            return (
                p.val == q.val
                and self.check(p.left, q.right)
                and self.check(p.right, q.left)
            )
        return p == q
