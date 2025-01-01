# 530. 二叉搜索树的最小绝对差
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.lastVal = None
        self.res = 10**5
        self.middleSort(root)
        return self.res

    def middleSort(self, root):
        if root is None:
            return None
        self.middleSort(root.left)
        if self.lastVal is None:
            self.lastVal = root.val
        else:
            self.res = min(self.res, root.val - self.lastVal)
            self.lastVal = root.val
        self.middleSort(root.right)
