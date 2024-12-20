# 173. 二叉搜索树迭代器
# 实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
# BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
# boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
# int next()将指针向右移动，然后返回指针处的数字。
# 注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。
# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class BSTIterator(object):
#     def __init__(self, root):
#         """
#         :type root: Optional[TreeNode]
#         """
#         self.cur = 0
#         self.arr = []
#         self.middleOrder(root)
#         self.arr_len = len(self.arr)

#     def middleOrder(self, root):
#         if not root:
#             return
#         self.middleOrder(root.left)
#         self.arr.append(root.val)
#         self.middleOrder(root.right)
#         return

#     def next(self):
#         """
#         :rtype: int
#         """
#         if self.cur >= self.arr_len:
#             return []
#         self.cur += 1
#         return self.arr[self.cur - 1]

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         if self.cur >= self.arr_len:
#             return False
#         return True


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.cur = root
        self.stack = []

    def next(self):
        """
        :rtype: int
        """
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        res = self.stack.pop()
        self.cur = res.right
        return res.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur is not None or len(self.stack) != 0
