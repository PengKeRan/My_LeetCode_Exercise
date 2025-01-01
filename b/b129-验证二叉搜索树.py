# 98. 验证二叉搜索树
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.middleSort(root, -float("inf"), float("inf"))

    def middleSort(self, root, small, big):
        if root is None:
            return True
        if root.val <= small or root.val >= big:
            return False
        return self.middleSort(root.left, small, root.val) and self.middleSort(
            root.right, root.val, big
        )

    #     self.lastVal = None
    #     self.flag = True
    #     self.middleSort(root)
    #     return self.flag

    # def middleSort(self, root):
    #     if root is None or not self.flag:
    #         return
    #     self.middleSort(root.left)
    #     if not self.flag:
    #         return
    #     if self.lastVal is None:
    #         self.lastVal = root.val
    #     else:
    #         if self.lastVal >= root.val:
    #             self.flag = False
    #         self.lastVal = root.val
    #     self.middleSort(root.right)
