// 79. 单词搜索
class Exist {
    boolean[][] walked;
    int row, col;

    public boolean exist(char[][] board, String word) {
        row = board.length;
        col = board[0].length;
        walked = new boolean[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (dfs(0, i, j, word, board)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(int pos, int i, int j, String word, char[][] board) {
        if (pos == word.length()) {
            return true;
        }
        if (i < 0 || j < 0 || i >= row || j >= col || walked[i][j] || board[i][j] != word.charAt(pos)) {
            return false;
        }
        walked[i][j] = true;
        if (dfs(pos + 1, i - 1, j, word, board) ||
                dfs(pos + 1, i, j - 1, word, board) ||
                dfs(pos + 1, i + 1, j, word, board) ||
                dfs(pos + 1, i, j + 1, word, board)) {
            return true;
        }
        walked[i][j] = false;

        return false;
    }

    public static void main(String[] args) {
        char[][] board = {
                { 'A', 'B', 'C', 'E' },
                { 'S', 'F', 'C', 'S' },
                { 'A', 'D', 'E', 'E' },
        };
        Exist sol = new Exist();
        System.out.println(sol.exist(board, "ABC"));
    }
}