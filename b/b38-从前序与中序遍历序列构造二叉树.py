"""
105. 从前序与中序遍历序列构造二叉树
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def buildInorder(inorder):
            if len(inorder) == 0:
                return None
            root = TreeNode(val=preorder[0])
            index = inorder.index(preorder[0])
            preorder.remove(preorder[0])
            root.left = buildInorder(inorder[0:index])
            root.right = buildInorder((inorder[index+1:len(inorder)]))
            return root

        return buildInorder(inorder)

sol = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(sol.buildTree(preorder, inorder))