import java.util.*;

class MinWindow2 {

    public String minWindow(String s, String t) {
        Map<Character, Integer> target = new HashMap<>();
        for (char c : t.toCharArray()) {
            target.put(c, target.getOrDefault(c, 0) + 1);
        }

        int ansL = -1, ansR = s.length();
        int meet = 0;
        int left = 0;
        Map<Character, Integer> memo = new HashMap<>();
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (target.containsKey(c)) {
                memo.put(c, memo.getOrDefault(c, 0) + 1);
                if (memo.get(c).equals(target.get(c))) {
                    meet += 1;
                }
            }
            char l;
            while (meet == target.size()) {
                if (right - left < ansR - ansL) {
                    ansL = left;
                    ansR = right;
                }
                l = s.charAt(left);
                if (target.containsKey(l)) {
                    if (memo.get(l).equals(target.get(l))) {
                        meet -= 1;
                    }
                    memo.put(l, memo.get(l) - 1);
                }
                left += 1;
            }
        }
        return ansL < 0 ? "" : s.substring(ansL, ansR + 1);
    }

    public static void main(String[] args) {
        MinWindow2 sol = new MinWindow2();
        String s = "ADOBECODEBANC";
        String t = "ABC";
        System.out.println(sol.minWindow(s, t));
    }
}