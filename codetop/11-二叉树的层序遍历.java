import java.util.*;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {

    public class TreeNode {

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

    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        List<List<Integer>> res = new ArrayList<>();
        Queue<TreeNode> arr = new LinkedList<>();
        arr.add(root);
        int len = arr.size();
        while (len > 0) {
            List<Integer> temp = new ArrayList<>();
            for (int i = 0; i < len; i++) {
                TreeNode node = arr.poll();
                temp.add(node.val);
                if (node.left != null) {
                    arr.add(node.left);
                }
                if (node.right != null) {
                    arr.add(node.right);
                }
            }
            res.add(temp);
            len = arr.size();
        }
        return res;
    }
}