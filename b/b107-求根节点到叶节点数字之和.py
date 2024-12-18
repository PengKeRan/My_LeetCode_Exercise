# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = [0]

        def getStr(root, s):
            newS = s + str(root.val)
            if not root.left and not root.right:
                res[0] += int(newS)
                return
            if root.left:
                getStr(root.left, newS)
            if root.right:
                getStr(root.right, newS)

        getStr(root, "")
        return res[0]
