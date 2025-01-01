# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        if root is None:
            return None
        self.cnt = 0
        self.res = 0
        self.k = k
        self.middleSort(root)
        return self.res

    def middleSort(self, root):
        if self.k <= 0 or root is None:
            return
        self.middleSort(root.left)
        if self.k <= 0:
            return
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.middleSort(root.right)
