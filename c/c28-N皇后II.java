import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class TotalNQueens {
    int n;
    int result;
    boolean[] cols, diag1, diag2;

    public int totalNQueens(int n) {
        this.n = n;
        this.result = 0;
        this.cols = new boolean[n];
        this.diag1 = new boolean[n * 2 - 1];
        this.diag2 = new boolean[n * 2 - 1];
        bfs(0);
        return this.result;
    }

    private void bfs(int row) {
        if (row == n) {
            result += 1;
            return;
        }
        for (int col = 0; col < n; col++) {
            if (cols[col] || diag1[n - 1 - row + col] || diag2[row + col]) {
                continue;
            }
            cols[col] = diag1[n - 1 - row + col] = diag2[row + col] = true;
            bfs(row + 1);
            cols[col] = diag1[n - 1 - row + col] = diag2[row + col] = false;
        }
    }

    // int n;
    // int result;

    // public int totalNQueens(int n) {
    // this.n = n;
    // this.result = 0;
    // bfs(n, 0, 0, new ArrayList<>());
    // return this.result;
    // }

    // private void bfs(int queen_num, int row_start, int col_start,
    // List<List<Integer>> seq) {
    // if (queen_num == 0) {
    // this.result += 1;
    // return;
    // }
    // if (row_start >= this.n || col_start >= this.n) {
    // return;
    // }
    // for (int i = row_start; i < n; i++) {
    // for (int j = col_start; j < n; j++) {
    // seq.add(new ArrayList<>(Arrays.asList(i, j)));
    // if (legal_queens(seq)) {
    // bfs(queen_num - 1, i + 1, 0, seq);
    // }
    // seq.remove(seq.size() - 1);
    // }
    // }
    // }

    // private boolean legal_queens(List<List<Integer>> seq) {
    // for (int i = 0; i < seq.size() - 1; i++) {
    // for (int j = i + 1; j < seq.size(); j++) {
    // int x1 = seq.get(i).get(0);
    // int y1 = seq.get(i).get(1);
    // int x2 = seq.get(j).get(0);
    // int y2 = seq.get(j).get(1);
    // if (y1 == y2 || Math.abs(x1 - x2) == Math.abs(y1 - y2)) {
    // return false;
    // }
    // }
    // }
    // return true;
    // }

    public static void main(String[] args) {
        int n = 4;
        TotalNQueens sol = new TotalNQueens();
        System.err.println(sol.totalNQueens(n));
    }
}
