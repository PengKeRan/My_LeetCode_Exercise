# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        layer = [root]
        while layer:
            length = len(layer)
            for i in range(length):
                node = layer[i]
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            res.append(layer[-1].val)
            layer = layer[length:]
        return res
