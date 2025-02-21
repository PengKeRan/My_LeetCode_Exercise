import java.util.*;

class WordBreak {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        int m = wordDict.size();
        int[] res = new int[n + 1];
        int[] wordLen = new int[m];
        int i, j;
        for (i = 1; i < n + 1; i++) {
            res[i] = n + 1;
        }
        for (i = 0; i < m; i++) {
            wordLen[i] = wordDict.get(i).length();
        }

        for (i = 0; i < n + 1; i++) {
            for (j = 0; j < m; j++) {
                if (wordLen[j] > i) {
                    continue;
                }
                if (wordDict.get(j).equals(s.substring(i - wordLen[j], i))) {
                    res[i] = Math.min(res[i - wordLen[j]] + 1, res[i]);
                }
            }
        }
        return res[n] != n + 1;
    }

    public static void main(String[] args) {
        String s = "leetcode";
        List<String> wordDict = new ArrayList<>();
        wordDict.add("leet");
        wordDict.add("code");
        WordBreak sol = new WordBreak();
        System.out.println(sol.wordBreak(s, wordDict));
    }
}