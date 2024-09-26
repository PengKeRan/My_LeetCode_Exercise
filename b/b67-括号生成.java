// 22. 括号生成
// 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

import java.util.ArrayList;
import java.util.List;

class GenerateParenthesis {
    private ArrayList[] memo = new ArrayList[100];

    public List<String> generateParenthesis(int n) {
        return generate(n);
    }

    private List<String> generate(int n) {
        if (memo[n] != null) {
            return memo[n];
        }
        ArrayList<String> ans = new ArrayList<String>();
        if (n == 0) {
            ans.add("");
        } else {
            for (int i = 0; i < n; i++) {
                for (String a : generate(n - 1 - i)) {
                    for (String b : generate(i)) {
                        ans.add("(" + a + ")" + b);
                    }
                }
            }
        }
        memo[n] = ans;
        return ans;
    }

    public static void main(String[] args) {
        GenerateParenthesis sol = new GenerateParenthesis();
        int n = 3;
        List<String> res = sol.generateParenthesis(n);
        for (String r : res) {
            System.out.println(r);
        }
    }
}
