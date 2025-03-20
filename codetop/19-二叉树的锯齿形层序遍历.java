
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
import java.util.*;

class Solution {
    // private static class TreeNode {
    // int val;
    // TreeNode left;
    // TreeNode right;

    // TreeNode() {
    // }

    // TreeNode(int val) {
    // this.val = val;
    // }

    // TreeNode(int val, TreeNode left, TreeNode right) {
    // this.val = val;
    // this.left = left;
    // this.right = right;
    // }
    // }

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        List<TreeNode> levelList = new ArrayList<>();
        List<Integer> levelRes = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        levelList.add(root);
        // levelRes.add(root.val);
        // res.add(levelRes);
        int order = 1;
        int len;
        while (levelList.size() > 0) {
            levelRes = new ArrayList<>();
            len = levelList.size();
            for (int i = 0; i < len; i++) {
                TreeNode node = levelList.get(0);
                if (order == 1) {
                    levelRes.add(node.val);
                } else {
                    levelRes.add(0, node.val);
                }
                if (node.left != null) {
                    levelList.add(node.left);
                }
                if (node.right != null) {
                    levelList.add(node.right);
                }
                levelList.remove(0);
            }
            order = 1 - order;
            res.add(levelRes);
        }

        return res;
    }
}