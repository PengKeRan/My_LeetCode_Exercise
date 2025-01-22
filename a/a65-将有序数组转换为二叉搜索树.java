// 108. 将有序数组转换为二叉搜索树
/**
 * Definition for a binary tree node.
 */

class SortedArrayToBST {
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

    public TreeNode sortedArrayToBST(int[] nums) {
        int n = nums.length;
        if (n == 0) {
            return null;
        }
        int midRoot = n / 2;
        int[] leftArr = new int[midRoot];
        int[] rightArr = new int[n - midRoot - 1];
        int i;
        for (i = 0; i < midRoot; i++) {
            leftArr[i] = nums[i];
        }
        for (i = midRoot + 1; i < n; i++) {
            rightArr[i - midRoot - 1] = nums[i];
        }
        TreeNode root = new TreeNode(nums[midRoot]);
        root.left = sortedArrayToBST(leftArr);
        root.right = sortedArrayToBST(rightArr);
        return root;
    }
}
