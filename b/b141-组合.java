import java.util.List;
import java.util.ArrayList;

class Combine {
    List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> combine(int n, int k) {
        bfs(1, n, k, new ArrayList<Integer>());
        return this.result;
    }

    private void bfs(int start, int n, int k, List<Integer> seq) {
        if (k == 0) {
            this.result.add(new ArrayList<>(seq));
            return;
        }
        for (int i = start; i <= n; i++) {
            seq.add(i);
            bfs(i + 1, n, k - 1, seq);
            seq.remove(seq.size() - 1);
        }
    }

    public static void main(String[] args) {
        int n = 4;
        int k = 2;
        Combine sol = new Combine();
        System.err.println(sol.combine(n, k));
    }
}
