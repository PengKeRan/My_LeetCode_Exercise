// 297. 二叉树的序列化与反序列化
// 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
// 同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
// 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
// 你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
// 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
// 你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

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

class Serialize {

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
        Serialize sol = new Serialize();
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