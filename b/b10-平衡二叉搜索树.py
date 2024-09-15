"""
1382. 将二叉搜索树变平衡
给你一棵二叉搜索树，请你返回一棵平衡后的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。如果有多种构造方法，请你返回任意一种。
如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是平衡的 。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 方法1：重组二叉树，先中序遍历
class Solution(object):
    # 中序遍历二叉树
    def inOrder(self, root):
        if root is None:
            return []
        ls = []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)

    # 根据序列生成平衡二叉树
    def buildTree(self, ls):
        if len(ls) == 0:
            return None
        mid_index = len(ls) // 2
        node = TreeNode(val=ls[mid_index], left=None, right=None)
        node.left = self.buildTree(ls[0:mid_index])
        node.right = self.buildTree(ls[mid_index + 1:len(ls)])
        return node

    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ls = self.inOrder(root)
        return self.buildTree(ls)


# 方法2：在原有二叉树基础上变化，时间复杂度太大
class Solution2(object):
    # 计算树的高度
    def height(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return max(self.height(root.left), self.height(root.right)) + 1

    # 平衡二叉树的旋转操作
    def averageTree(self, root):
        # 情况1，左子树比右子树高2以上,且左子树的左子树比左子树的右子树更高
        if self.height(root.left) > self.height(root.right) and self.height(root.left.left) > self.height(
                root.left.right):
            temp = root.left
            root.left = root.left.right
            temp.right = root
            root = temp
        # 情况2，左子树比右子树高2以上,且左子树的右子树比左子树的左子树更高
        if self.height(root.left) > self.height(root.right) and self.height(root.left.left) < self.height(
                root.left.right):
            temp = root.left.right
            root.left.right = temp.left
            temp.left = root.left
            root.left = temp.right
            temp.right = root
            root = temp

        # 情况3，右子树比左子树高2以上,且右子树的右子树比右子树的右子树更高
        if self.height(root.left) < self.height(root.right) and self.height(root.right.left) < self.height(
                root.right.right):
            temp = root.right
            root.right = root.right.left
            temp.left = root
            root = temp

        # 情况4，右子树比左子树高2以上,且右子树的左子树比右子树的左子树更高
        if self.height(root.left) < self.height(root.right) and self.height(root.right.left) > self.height(
                root.right.right):
            temp = root.right.left
            root.right.left = temp.right
            temp.right = root.right
            root.right = temp.left
            temp.left = root
            root = temp
        return root

    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if abs(self.height(root.left) - self.height(root.right)) < 1:
            return root

        while abs(self.height(root.left) - self.height(root.right)) > 1:
            root = self.averageTree(root)

        if root.left is not None:
            root.left = self.balanceBST(root.left)
        if root.right is not None:
            root.right = self.balanceBST(root.right)

        return root


root = TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=TreeNode(val=3, left=None,
                                                                                  right=TreeNode(val=4, left=None,
                                                                                                 right=None))))
sol = Solution()
print(sol.inOrder(root))
