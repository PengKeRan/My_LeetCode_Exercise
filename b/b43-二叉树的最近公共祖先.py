# 236, 二叉树的最近公共祖先
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # path_p = self.get_path([root.val], root, p.val)
        # path_q = self.get_path([root.val], root, q.val)
        # print(path_p)
        # print(path_q)
        # for i in range(min(len(path_p), len(path_q))):
        #     if path_p[i] != path_q[i]:
        #         return path_p[i - 1]
        # if len(path_p) < len(path_q):
        #     if path_p[-1] == path_q[len(path_p) - 1]:
        #         return path_p[-1]
        # if len(path_q) < len(path_p):
        #     if path_q[-1] == path_p[len(path_q) - 1]:
        #         return path_q[-1]
        # return
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None:
            return right
        if right is None:
            return left
        return root

    def get_path(self, path, root, p):
        path_L = path
        path_R = list(path)
        if root.val == p:
            return path
        else:
            if root.left:
                path_L.append(root.left.val)
                res = self.get_path(path_L, root.left, p)
                if res:
                    return res
            if root.right:
                path_R.append(root.right.val)
                res = self.get_path(path_R, root.right, p)
                if res:
                    return res

    def get_height(self, root, p):
        h = 0
        queue = [root]
        while len(queue) > 0:
            l = len(queue)
            for node in queue:
                if node.val == p:
                    return h
            for i in range(l):
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            h += 1
            queue = queue[l:]


sol = Solution()
root = TreeNode(val=3, left=TreeNode(val=5, left=TreeNode(val=6, left=None, right=None),
                                     right=TreeNode(val=2, left=TreeNode(val=7, left=None, right=None),
                                                    right=TreeNode(val=4, left=None, right=None))),
                right=TreeNode(val=1, left=TreeNode(val=0, left=None, right=None),
                               right=TreeNode(val=8, left=None, right=None)))
p = TreeNode(val=5)
q = TreeNode(val=1)
print(sol.lowestCommonAncestor(root, p, q))
