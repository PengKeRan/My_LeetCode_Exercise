class LongestPalindrome2 {
    public String longestPalindrome(String s) {
        if (s.length() == 1) {
            return s;
        }
        StringBuilder t = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            t.append(s.charAt(i));
            t.append("#");
        }
        s = t.toString();
        int n = s.length();
        int[] dp = new int[n];
        int center = -1;
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            while (i - dp[i] >= 0 && i + dp[i] < n && s.charAt(i - dp[i]) == s.charAt(i + dp[i])) {
                dp[i]++;
            }
            if (dp[i] > maxLen) {
                maxLen = dp[i];
                center = i;
            }
        }
        StringBuilder r = new StringBuilder();
        for (int i = center - maxLen + 1; i < center + maxLen; i++) {
            if (s.charAt(i) != '#') {
                r.append(s.charAt(i));
            }
        }
        return r.toString();
    }

    public static void main(String[] args) {
        String s = "cbbd";
        LongestPalindrome2 sol = new LongestPalindrome2();
        System.out.println(sol.longestPalindrome(s));
    }
}