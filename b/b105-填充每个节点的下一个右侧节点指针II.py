# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        layer = [root]
        nextLayer = []
        while layer:

            for i in range(len(layer) - 1):
                layer[i].next = layer[i + 1]
            layer[-1].next = None
            layer = nextLayer
            nextLayer = []
            for node in layer:
                if node.left is not None:
                    nextLayer.append(node.left)
                if node.right is not None:
                    nextLayer.append(node.right)

        return root
