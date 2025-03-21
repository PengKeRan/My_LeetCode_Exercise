class LongestPalindrome2 {
    public String longestPalindrome(String s) {
        int n = s.length();
        int centerL = 0, centerR = 0;
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            int odd = expand(s, i, i, n);
            if (odd > maxLen) {
                centerL = i;
                centerR = i;
                maxLen = odd;
            }
            int even = expand(s, i, i + 1, n);
            if (even >= maxLen) {
                centerL = i;
                centerR = i + 1;
                maxLen = even;
            }
        }
        return s.substring(centerL - maxLen, centerR + maxLen + 1);
    }

    private int expand(String s, int centerL, int centerR, int n) {
        int len = 0;
        if (centerL < 0 || centerR >= n) {
            return -1;
        }
        for (int i = 0; i < n; i++) {
            len = i - 1;
            if (centerL - i < 0 || centerR + i >= n) {
                break;
            }
            if (s.charAt(centerL - i) != s.charAt(centerR + i)) {
                break;
            }
        }
        return len;
    }

    public static void main(String[] args) {
        String s = "cbbd";
        LongestPalindrome2 sol = new LongestPalindrome2();
        System.out.println(sol.longestPalindrome(s));
    }
}