# 104. 二叉树的最大深度
# 给定一个二叉树 root ，返回其最大深度。
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


sol = Solution()
root = TreeNode(val=3, left= TreeNode(val= 9, left= None, right= None), right= TreeNode(val= 20, left= TreeNode(val= 15, left= None, right= None), right= TreeNode(val= 7, left= None, right= None)))

print(sol.maxDepth(root))