// 98. 验证二叉搜索树 
// 给你一个二叉树的根节点 root，判断其是否是一个有效的二叉搜索树。
// 有效 二叉搜索树定义如下：
// 节点的左 子树 只包含 小于 当前节点的数。节点的右子树只包含 大于 当前节点的数。所有左子树和右子树自身必须也是二叉搜索树。

import java.util.*;

class IsValidBST {
    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    // 1、中序遍历，再遍历输出序列
    // private List<Integer> order;

    // private void middle(TreeNode root) {
    // if (root == null) {
    // return;
    // }
    // if (root.left != null) {
    // middle(root.left);
    // }
    // order.add(root.val);
    // if (root.right != null) {
    // middle(root.right);
    // }
    // return;
    // }

    // public boolean isValidBST(TreeNode root) {
    // order = new ArrayList<>();
    // middle(root);
    // int n = order.size();
    // if (n <= 1) {
    // return true;
    // }
    // // for (int i = 0; i < n - 1; i++) {
    // // if (order.get(i) >= order.get(i + 1)) {
    // // return false;
    // // }
    // // }
    // return true;
    // }

    // 2
    private boolean check(TreeNode root, long small, long big) {

        if (root == null) {
            return true;
        }

        if (root.val >= big || root.val <= small) {
            return false;
        }
        return check(root.left, small, root.val) && check(root.right, root.val, big);
    }

    // 2147483647
    public boolean isValidBST(TreeNode root) {
        return check(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    // 3、中序遍历，增添的时候判断
    // private List<Integer> order;

    // private boolean middle(TreeNode root) {
    // if (root == null) {
    // return true;
    // }
    // if (!middle(root.left))
    // return false;
    // order.add(root.val);
    // int idx = order.size() - 1;
    // if (idx >= 1) {
    // if (order.get(idx) <= order.get(idx - 1))
    // return false;
    // }
    // if (!middle(root.right))
    // return false;
    // return true;
    // }

    // public boolean isValidBST(TreeNode root) {
    // order = new ArrayList<>();
    // if (!middle(root))
    // return false;
    // return true;
    // }

    public static void main(String[] args) {
        IsValidBST sol = new IsValidBST();
        TreeNode root = new TreeNode(4);
        TreeNode left = new TreeNode(1);
        TreeNode right = new TreeNode(6);
        // TreeNode rightleft = new TreeNode(5);
        // TreeNode rightright = new TreeNode(7);
        // right.left = rightleft;
        // right.right = rightright;
        root.left = left;
        root.right = right;
        System.out.println(sol.isValidBST(root));
    }
}
