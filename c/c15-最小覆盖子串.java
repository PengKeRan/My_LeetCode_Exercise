// 76. 最小覆盖子串 
// 给你一个字符串 s、一个字符串 t。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串""。

class MinWindow {
    public String minWindow(String s, String t) {
        return null;
    }

    public static void main(String[] args) {
        MinWindow sol = new MinWindow();
        String s = "ADOBECODEBANC", t = "ABC";
        System.out.println(sol.minWindow(s, t));
    }
}
