
// 102. 二叉树的层序遍历 
// 给你二叉树的根节点 root，返回其节点值的 层序遍历。（即逐层地，从左到右访问所有节点）。
import java.util.*;

class LevelOrder {

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

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null)
            return ans;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            List<Integer> temp = new ArrayList<>();
            int queueLen = queue.size();

            for (int i = 0; i < queueLen; i++) {
                TreeNode node = queue.poll();
                temp.add(node.val);
                if (node.left != null) {
                    queue.add(node.left);
                }
                if (node.right != null) {
                    queue.add(node.right);
                }
            }
            ans.add(temp);
        }

        return ans;
    }

    public static void main(String[] args) {
        LevelOrder sol = new LevelOrder();
        TreeNode root = new TreeNode(3);
        TreeNode left = new TreeNode(9);
        TreeNode rightleft = new TreeNode(15);
        TreeNode rightright = new TreeNode(7);
        TreeNode right = new TreeNode(20);
        right.left = rightleft;
        right.right = rightright;
        root.left = left;
        root.right = right;
        System.out.println(sol.levelOrder(root));
    }
}
