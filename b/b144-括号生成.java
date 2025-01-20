import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

// 22. 括号生成
class GenerateParenthesis {
    List<String> res;

    public List<String> generateParenthesis(int n) {
        res = new ArrayList<>();
        dfs(n, n, new StringBuilder());
        return res;
    }

    private void dfs(int left, int right, StringBuilder parren) {
        if (left == 0 && right == 0) {
            res.add(parren.toString());
        }
        if (left > right) {
            return;
        }
        if (left > 0) {
            parren.append("(");
            dfs(left - 1, right, parren);
            parren.deleteCharAt(parren.length() - 1);
        }
        if (right > 0) {
            parren.append(")");
            dfs(left, right - 1, parren);
            parren.deleteCharAt(parren.length() - 1);
        }
    }
    // public List<String> generateParenthesis(int n) {
    // res = new ArrayList<>();
    // dfs(n * 2, 0, "");
    // return res;
    // }

    // private void dfs(int total, int score, String parren) {
    // if (total == 0 && score == 0) {
    // res.add(parren);
    // }
    // if (score < 0 || score > total) {
    // return;
    // }
    // dfs(total - 1, score + 1, parren + "(");
    // dfs(total - 1, score - 1, parren + ")");
    // }

    public static void main(String[] args) {
        int n = 3;
        GenerateParenthesis sol = new GenerateParenthesis();
        System.out.println(sol.generateParenthesis(n));
    }
}