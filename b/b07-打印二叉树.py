"""
剑指 Offer 32 - I. 从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        children = [root]
        while len(children)>0:
            res.append(children[0].val)
            if children[0].left is not None:
                children.append(children[0].left)
            if children[0].right is not None:
                children.append(children[0].right)
            children.pop(0)
        return res


sol = Solution()
tree = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4, left=None, right=None),
                                     right=TreeNode(val=5, left=None, right=None)),
                right=TreeNode(val=3, left=TreeNode(val=6, left=None, right=None),
                               right=TreeNode(val=7, left=None, right=None)))
print(sol.levelOrder(tree))
