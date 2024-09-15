"""
437. 路径总和 III

给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    count = 0
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if root is None:
            return 0
        # 1.前缀和（从头到尾）
        hashmap = {0: 1}
        pre = 0
        self.front(root, pre, hashmap, targetSum)
        return self.count

        # 2.递归
        # if root is None:
        #     return 0
        # self.through(root, targetSum, 0)
        # self.pathSum(root.left, targetSum)
        # self.pathSum(root.right, targetSum)
        #
        # return self.count

    def front(self, root, pre, hashmap, targetSum):
        if root is None:
            return

        pre += root.val
        if pre - targetSum in hashmap:
            self.count += hashmap[pre - targetSum]
        if pre in hashmap:
            hashmap[pre] += 1
        else:
            hashmap[pre] = 1

        self.front(root.left, pre, hashmap, targetSum)
        self.front(root.right, pre, hashmap, targetSum)

        hashmap[pre] -= 1

    def through(self, root, targetSum, total):
        if root is None:
            return
        total += root.val
        if total == targetSum:
            self.count += 1
        self.through(root.left, targetSum, total)
        self.through(root.right, targetSum, total)
        pass


sol = Solution()
root1 = TreeNode(val=10, left=TreeNode(val=5, left=TreeNode(val=3, left=TreeNode(val=3, left=None, right=None),
                                                            right=TreeNode(val=-2, left=None, right=None)),
                                       right=TreeNode(val=2, left=None, right=TreeNode(val=1, left=None, right=None))),
                 right=TreeNode(val=-3, left=None, right=TreeNode(val=11, left=None, right=None)))
targetSum1 = 8
print(sol.pathSum(root1, targetSum1))
