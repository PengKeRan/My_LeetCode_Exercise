# 102. 二叉树的层序遍历
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        layer = [root]
        temp = [root.val]
        while layer:
            length = len(layer)
            res.append(temp)
            temp = []
            for i in range(length):
                node = layer[i]
                if node.left:
                    layer.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    layer.append(node.right)
                    temp.append(node.right.val)
            layer = layer[length:]
        return res
