"""
538.把二叉搜索树转换为累加树 和 1038相同
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node的新值等于原树中大于或等于node.val的值之和。
提醒一下，二叉搜索树满足下列约束条件：
节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        origin_val = []
        new_val = []
        num = 0
        def inOrder(root):
            nonlocal num
            if root.right is not None:
                inOrder(root.right)
            root.val += num
            num = root.val
            if root.left is not None:
                inOrder(root.left)
        inOrder(root)
        # for i in range(len(origin_val)):
        #     new_val.append(sum(origin_val[0:i+1]))
        #
        # def changeVal(root):
        #     if root.right is not None:
        #         changeVal(root.right)
        #     for i in range(len(origin_val)):
        #         if root.val==origin_val[i]:
        #             root.val=new_val[i]
        #             break
        #     if root.left is not None:
        #         changeVal(root.left)
        # changeVal(root)
        return root


sol = Solution()
root1 = TreeNode(val=4, left=TreeNode(val=1, left=TreeNode(val=0, left=None, right=None),
                                      right=TreeNode(val=2, left=None, right=TreeNode(val=3, left=None, right=None))),
                 right=TreeNode(val=6, left=TreeNode(val=5, left=None, right=None),
                                right=TreeNode(val=7, left=None, right=TreeNode(val=8, left=None, right=None))))
sol.convertBST(root1)
