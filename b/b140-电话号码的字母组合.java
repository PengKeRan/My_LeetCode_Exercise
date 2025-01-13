import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;

class LetterCombinations {
    List<String> res = new ArrayList<>();
    // HashMap<Character, String[]> memo = new HashMap<>();
    String[] map = {
            "", // 0
            "", // 1
            "abc", // 2
            "def", // 3
            "ghi", // 4
            "jkl", // 5
            "mno", // 6
            "pqrs", // 7
            "tuv", // 8
            "wxyz" // 9
    };

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return this.res;
        }
        // this.memo.put('2', new String[] { "a", "b", "c" });
        // this.memo.put('3', new String[] { "d", "e", "f" });
        // this.memo.put('4', new String[] { "g", "h", "i" });
        // this.memo.put('5', new String[] { "j", "k", "l" });
        // this.memo.put('6', new String[] { "m", "n", "o" });
        // this.memo.put('7', new String[] { "p", "q", "r", "s" });
        // this.memo.put('8', new String[] { "t", "u", "v" });
        // this.memo.put('9', new String[] { "w", "x", "y", "z" });

        dfs(digits, 0, new StringBuilder());
        return this.res;
    }

    private void dfs(String digits, int idx, StringBuilder preffix) {
        if (idx == digits.length()) {
            this.res.add(preffix.toString());
            return;
        }
        String letters = map[digits.charAt(idx) - '0'];
        for (char ch : letters.toCharArray()) {
            preffix.append(ch); // 添加当前字符
            dfs(digits, idx + 1, preffix);
            preffix.deleteCharAt(preffix.length() - 1); // 添加当前字符
        }
    }

    public static void main(String[] args) {
        String digits = "23";
        LetterCombinations sol = new LetterCombinations();
        System.err.println(sol.letterCombinations(digits));
    }
}