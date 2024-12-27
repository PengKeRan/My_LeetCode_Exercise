# 637. 二叉树的层平均值
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if root is None:
            return []
        res = []
        layer = [root]
        total = root.val
        while layer:
            length = len(layer)
            res.append(total / float(length))
            total = 0

            for i in range(length):
                node = layer[i]
                if node.left:
                    layer.append(node.left)
                    total += node.left.val
                if node.right:
                    layer.append(node.right)
                    total += node.right.val
            layer = layer[length:]
        return res
