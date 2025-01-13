import java.util.ArrayList;
import java.util.List;

class FindWords {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        String word = null; // 如果当前节点是单词结尾，则存储该单词
    }

    private TrieNode buildTrie(String[] words) {
        TrieNode root = new TrieNode();
        for (String word : words) {
            TrieNode node = root;
            for (char ch : word.toCharArray()) {
                int idx = ch - 'a';
                if (node.children[idx] == null) {
                    node.children[idx] = new TrieNode();
                }
                node = node.children[idx];
            }
            node.word = word; // 标记单词结尾
        }
        return root;
    }

    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = buildTrie(words);
        List<String> res = new ArrayList<>();
        int m = board.length, n = board[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dfs(board, i, j, root, res);
            }
        }
        return res;
    }

    private void dfs(char[][] board, int i, int j, TrieNode node, List<String> res) {
        char ch = board[i][j];
        if (ch == '#' || node.children[ch - 'a'] == null) {
            return; // 无效路径或当前字符不匹配
        }

        node = node.children[ch - 'a'];
        if (node.word != null) {
            res.add(node.word); // 找到单词
            node.word = null; // 防止重复添加
        }

        // 标记当前位置为访问过
        board[i][j] = '#';

        // 向四个方向递归搜索
        if (i > 0)
            dfs(board, i - 1, j, node, res);
        if (j > 0)
            dfs(board, i, j - 1, node, res);
        if (i < board.length - 1)
            dfs(board, i + 1, j, node, res);
        if (j < board[0].length - 1)
            dfs(board, i, j + 1, node, res);

        // 恢复当前位置的字符
        board[i][j] = ch;
    }
    // public List<String> findWords(char[][] board, String[] words) {
    // int m = board.length;
    // int n = board[0].length;
    // boolean[][] walked = new boolean[m][n];
    // List<String> res = new ArrayList<>();
    // for (String word : words) {
    // boolean flag = false;
    // for (int i = 0; i < m; i++) {
    // for (int j = 0; j < n; j++) {
    // if (subFind(board, i, j, word, 0, walked)) {
    // res.add(word);
    // flag = true;
    // break;
    // }
    // }
    // if (flag) {
    // break;
    // }
    // }
    // }
    // return res;
    // }

    // private boolean subFind(char[][] board, int i, int j, String word, int idx,
    // boolean[][] walked) {
    // if (idx == word.length()) {
    // return true;
    // }
    // if (i < 0 || i >= board.length || j < 0 || j >= board[0].length ||
    // board[i][j] != word.charAt(idx)
    // || walked[i][j]) {
    // return false;
    // }
    // walked[i][j] = true;
    // boolean res = subFind(board, i - 1, j, word, idx + 1, walked) ||
    // subFind(board, i + 1, j, word, idx + 1, walked)
    // || subFind(board, i, j - 1, word, idx + 1, walked) || subFind(board, i, j +
    // 1, word, idx + 1, walked);
    // walked[i][j] = false;

    // return res;
    // }

    public static void main(String[] args) {
        char[][] board = {
                { 'a', 'b', 'c' },
                { 'a', 'e', 'd' },
                { 'a', 'f', 'g' },
        };
        FindWords solution = new FindWords();
        System.out.println(solution.findWords(board, new String[] { "eaafgdcba" }));
    }
}