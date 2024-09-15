# 124. 二叉树中的最大路径和
# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。
# 同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.max_sum = -1000
        def contribute(r):
            if r is None:
                return 0
            left_contribute = max(contribute(r.left),0)
            right_contribute = max(contribute(r.right), 0)
            temp = r.val+left_contribute+right_contribute
            if self.max_sum < temp:
                self.max_sum = temp
            return r.val + max(left_contribute, right_contribute)
        contribute(root)
        return self.max_sum
        # dp[0] = max(0, dp.left[0], dp.left[1], dp.left[2], dp.right[0], dp.right[1], dp.right[2])
        # dp[1] = max(val + dp.left[1], val + dp.right[1], val)
        # dp[2] = val + dp.left[1] + dp.right[1]
        # inf = 1000
        # memo = dict()
        #
        # def dp(r):
        #     if r is None:
        #         return None
        #     if r.left not in memo.keys():
        #         left = dp(r.left)
        #         memo[r.left] = left
        #     else:
        #         left = memo[r.left]
        #     if r.right not in memo.keys():
        #         right = dp(r.right)
        #         memo[r.right] = right
        #     else:
        #         right = memo[r.right]
        #     if left is None and right is None:
        #         return [-inf, r.val, -inf * 2]
        #     if left is None or right is None:
        #         if left:
        #             num0 = max(left[0], left[1], left[2])
        #             num1 = max(r.val, r.val + left[1])
        #         if right:
        #             num0 = max(right[0], right[1], right[2])
        #             num1 = max(r.val, r.val + right[1])
        #         return [num0, num1, -inf]
        #     num0 = max(left[0], left[1], left[2], right[0], right[1], right[2])
        #     num1 = max(r.val + left[1], r.val + right[1], r.val)
        #     num2 = r.val + left[1] + right[1]
        #     return [num0, num1, num2]
        #
        # return max(dp(root))






sol = Solution()
root = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=TreeNode(val=3, left=None, right=None))
root = TreeNode(val=-2, left=TreeNode(val=1, left=None, right=None))
root = TreeNode(val=5, left=None, right=TreeNode(val=-2, left=TreeNode(val=1, left=None, right=None),
                                                 right=TreeNode(val=-1, left=None,
                                                                right=TreeNode(val=4, left=None, right=None))))
print(sol.maxPathSum(root))
