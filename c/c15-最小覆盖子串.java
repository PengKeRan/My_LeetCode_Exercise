
// 76. 最小覆盖子串 
// 给你一个字符串 s、一个字符串 t。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串""。
import java.util.*;

class MinWindow {
    public String minWindow(String s, String t) {
        Map<Character, Integer> target_map = new HashMap<>();
        Map<Character, Integer> window_map = new HashMap<>();
        for (Character c : t.toCharArray()) {
            target_map.put(c, target_map.getOrDefault(c, 0) + 1);
        }

        int left = 0, right = 0, n = s.length();
        int count = 0;
        int minlen = Integer.MAX_VALUE, minleft = 0;

        while (right < n) {
            Character rightChar = s.charAt(right);
            if (target_map.containsKey(rightChar)) { // 移右指针
                window_map.put(rightChar, window_map.getOrDefault(rightChar, 0) + 1);
                if (window_map.get(rightChar).equals(target_map.get(rightChar))) {
                    count++;
                }
            }
            right++;

            while (count == target_map.size()) {
                if (right - left < minlen) {
                    minlen = right - left;
                    minleft = left;
                }
                Character leftChar = s.charAt(left);
                if (target_map.containsKey(leftChar)) { // 移右指针
                    window_map.put(leftChar, window_map.getOrDefault(leftChar, 0) - 1);
                    if (window_map.get(leftChar) < target_map.get(leftChar)) {
                        count--;
                    }
                }
                left++;
            }
        }
        return minlen == Integer.MAX_VALUE ? "" : s.substring(minleft, minleft + minlen);
    }

    public static void main(String[] args) {
        MinWindow sol = new MinWindow();
        String s = "ADOBECODEBANC", t = "ABC";
        System.out.println(sol.minWindow(s, t));
    }
}
