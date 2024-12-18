# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def pathSum(root):
            # res[1]表示root在端点,res[0]不在
            res = [float("-inf"), float("-inf")]
            if not root:
                return res
            left = pathSum(root.left)
            right = pathSum(root.right)
            res[0] = max(
                max(left),
                max(right),
                left[1] + root.val + right[1],
            )
            res[1] = max(root.val, root.val + max(left[1], right[1]))
            return res

        return max(pathSum(root))

        # 改进：（方法一的res[0]很多余）
        # res = [float("-inf")]

        # def contribute(root):
        #     if not root:
        #         return 0
        #     left_contribute = max(contribute(root.left), 0)
        #     right_contribute = max(contribute(root.right), 0)
        #     temp = left_contribute + right_contribute + root.val
        #     res[0] = max(res[0], temp)
        #     return root.val + max(left_contribute, right_contribute)

        # contribute(root)
        # return res[0]
