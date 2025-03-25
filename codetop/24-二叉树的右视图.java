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

    public List<Integer> rightSideView(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        List<Integer> res = new ArrayList<>();
        List<TreeNode> level = new ArrayList<>();
        level.add(root);
        int len = 1;
        while (level.size() != 0) {
            len = level.size();
            res.add(level.get(len - 1).val);
            for (int i = 0; i < len; i++) {
                TreeNode temp = level.get(i);
                if (temp.left != null) {
                    level.add(temp.left);
                }
                if (temp.right != null) {
                    level.add(temp.right);
                }
            }
            level.forEach((e) -> {
                System.out.println(e.val);
            });
            level = level.subList(len, level.size());
        }
        return res;
    }

}