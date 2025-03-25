class Solution {

    private static class TreeNode {
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

    public int maxPathSum(TreeNode root) {
        int[] res = new int[2];
        res = pathSum(root);
        return Math.max(res[0], res[1]);
    }

    // 0:根节点为端点，1:否
    private int[] pathSum(TreeNode root) {
        int[] res = new int[2];
        if (root == null) {
            res[0] = Integer.MIN_VALUE;
            res[1] = Integer.MIN_VALUE;
            return res;
        }
        int[] l = pathSum(root.left);
        int[] r = pathSum(root.right);

        res[0] = root.val;
        if (l[0] != Integer.MIN_VALUE) {
            res[0] = Math.max(res[0], root.val + l[0]);
        }
        if (r[0] != Integer.MIN_VALUE) {
            res[0] = Math.max(res[0], root.val + r[0]);
        }

        res[1] = root.val;
        if (l[0] != Integer.MIN_VALUE && r[0] != Integer.MIN_VALUE) {
            res[1] = Math.max(root.val + l[0] + r[0], root.val);
        }
        res[1] = Math.max(res[1], l[1]);
        res[1] = Math.max(res[1], r[1]);
        res[1] = Math.max(res[1], l[0]);
        res[1] = Math.max(res[1], r[0]);

        return res;
    }
}