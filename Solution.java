import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Definition for a binary tree node.
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class Solution {
    // 前序遍历
    private String before(TreeNode root) {
        if (root == null) {
            return "None";
        }
        String left = before(root.left);
        String right = before(root.right);
        String res = String.valueOf(root.val);
        if (left != "") {
            res += "/" + left;
        }
        if (right != "") {
            res += "/" + right;
        }
        return res;
    }

    // "3/2/3/None/None/None/4/None/None"
    public TreeNode restoreTree(List<String> series) {
        if (series.get(0).equals("None")) {
            series.remove(0);
            return null;
        }

        TreeNode res = new TreeNode(Integer.valueOf(series.get(0)));
        series.remove(0);
        res.left = restoreTree(series);
        res.right = restoreTree(series);

        return res;
    }

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        String beforeStr = before(root);
        return beforeStr;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] series = data.split("/");
        List<String> list = new ArrayList<>(Arrays.asList(series));
        TreeNode res = restoreTree(list);

        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(4);
        root.right.right = new TreeNode(5);

        TreeNode root2 = new TreeNode(3);
        root2.left = new TreeNode(2);
        root2.right = new TreeNode(4);
        root2.left.left = new TreeNode(3);

        String series = sol.serialize(root2);
        System.out.println(series);
        TreeNode deSer = sol.deserialize(series);
        // System.out.println(sol.decodeString(s2));
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
