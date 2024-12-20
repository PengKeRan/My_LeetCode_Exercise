# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        cur = root
        l_h = 1
        while cur.left:
            l_h += 1
            cur = cur.left
        r_h = 1
        cur = root
        while cur.right:
            r_h += 1
            cur = cur.right

        if l_h == r_h:
            return 2**l_h - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    #     self.res = 0
    #     self.middleOrder(root)
    #     return self.res

    # def middleOrder(self, root):
    #     if not root:
    #         return
    #     self.middleOrder(root.left)
    #     self.res += 1
    #     self.middleOrder(root.right)
    #     return
