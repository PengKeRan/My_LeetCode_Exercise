# 337. 打家劫舍 III
# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
# 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
# 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # memo = dict()
        # def ds(root):
        #     if root in memo.keys():
        #         return memo[root]
        #     if root is None:
        #         return 0
        #     if root.left is None and root.right is None:
        #         memo[root] = root.val
        #         return root.val
        #     children_val = 0
        #     grand_children_val = 0
        #     if root.left:
        #         children_val += ds(root.left)
        #         grand_children_val += ds(root.left.left) + ds(root.left.right)
        #     if root.right:
        #         children_val += ds(root.right)
        #         grand_children_val += ds(root.right.left) + ds(root.right.right)
        #     memo[root] = max(root.val+grand_children_val, children_val)
        #     return memo[root]
        # return ds(root)

        def ds(r):  # 0:不选， 1：选
            result = [0, 0]
            if r is None:
                return result
            left_val = ds(r.left)
            right_val = ds(r.right)

            result[0] = max(left_val[0], left_val[1]) + max(right_val[0], right_val[1])
            result[1] = r.val + left_val[0] + right_val[0]
            return result
        return max(ds(root))


sol = Solution()
root = TreeNode(val=3, left=TreeNode(val=2, left=None, right=TreeNode(val=3, left=None, right=None)),
                right=TreeNode(val=3, left=None, right=TreeNode(val=1, left=None, right=None)))
print(sol.rob(root))
