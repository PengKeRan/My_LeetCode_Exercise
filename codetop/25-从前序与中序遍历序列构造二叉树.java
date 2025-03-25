import java.util.ArrayList;
import java.util.List;

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

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int n = preorder.length;
        return build(preorder, inorder, 0, n - 1, 0, n - 1);
    }

    private TreeNode build(int[] pre, int[] in, int pl, int pr, int il, int ir) {
        if (pr - pl != ir - il) {
            System.out.println("XXXXXXXXXXXXXXXX");
            return null;
        }
        if (pl > pr) {
            return null;
        }
        TreeNode root = new TreeNode(pre[pl]);
        if (pr == pl) {
            return root;
        }
        int idx = -1;
        for (int i = il; i <= ir; i++) {
            if (in[i] == pre[pl]) {
                idx = i;
                break;
            }
        }
        root.left = build(pre, in, pl + 1, pl + idx - il, il, idx - 1);
        root.right = build(pre, in, pl + idx - il + 1, pr, idx + 1, ir);
        return root;
    }

}