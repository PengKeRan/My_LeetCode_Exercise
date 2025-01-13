import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;

class LetterCombinations {
    List<String> res = new ArrayList<>();
    HashMap<Character, String[]> memo = new HashMap<>();

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return this.res;
        }
        this.res = new ArrayList<>();
        this.memo.put('2', new String[] { "a", "b", "c" });
        this.memo.put('3', new String[] { "d", "e", "f" });
        this.memo.put('4', new String[] { "g", "h", "i" });
        this.memo.put('5', new String[] { "j", "k", "l" });
        this.memo.put('6', new String[] { "m", "n", "o" });
        this.memo.put('7', new String[] { "p", "q", "r", "s" });
        this.memo.put('8', new String[] { "t", "u", "v" });
        this.memo.put('9', new String[] { "w", "x", "y", "z" });

        dfs(digits, 0, "");
        return this.res;
    }

    private void dfs(String digits, int idx, String preffix) {
        if (idx == digits.length()) {
            this.res.add(preffix);
            return;
        }
        for (String str : this.memo.get(digits.charAt(idx))) {
            dfs(digits, idx + 1, preffix + str);
        }
    }

    public static void main(String[] args) {
        String digits = "23";
        LetterCombinations sol = new LetterCombinations();
        System.err.println(sol.letterCombinations(digits));
    }
}