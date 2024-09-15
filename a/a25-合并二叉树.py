# 617. 合并二叉树
# 给你两棵二叉树： root1 和 root2 。
# 想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。
# 你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。
# 返回合并后的二叉树。
# 注意: 合并过程必须从两个树的根节点开始。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """

        def merge(r1, r2):
            if r1 is None and r2 is None:
                return None
            if r1 is None:
                return r2
            if r2 is None:
                return r1
            tempNode = TreeNode(val=r1.val + r2.val, left=merge(r1.left, r2.left), right=merge(r1.right, r2.right))
            return tempNode

        return merge(root1, root2)
