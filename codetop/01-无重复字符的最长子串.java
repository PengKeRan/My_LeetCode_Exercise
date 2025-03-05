import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> window = new HashSet<>();
        int left = 0, right = 0;
        int n = s.length();
        int ans = 0;
        while (right < n) {
            Character c = s.charAt(right);
            if (window.contains(c)) {
                while (left < right && s.charAt(left) != c) {
                    window.remove(s.charAt(left));
                    left++;
                }
                if (left < right) {
                    window.remove(s.charAt(left));
                    left++;
                }
            }
            window.add(c);
            right += 1;
            ans = Math.max(ans, right - left);
        }
        return ans;
    }

    public static void main(String[] args) {
        String s = "pwwkew";
        Solution sol = new Solution();
        System.out.println(sol.lengthOfLongestSubstring(s));
    }
}