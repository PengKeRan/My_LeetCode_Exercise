// LCR 002. 二进制求和
// 给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。
// 输入为 非空 字符串且只包含数字 1 和 0。

class AddBinary {
    public String addBinary(String a, String b) {
        String ans = "";
        int plus = 0;
        int a_len = a.length();
        int b_len = b.length();
        int temp = 0;
        int i;
        for (i = 0; i < Math.max(a_len, b_len); i++) {
            if (i < Math.min(a_len, b_len)) {
                temp = Character.getNumericValue(a.charAt(a_len - 1 - i)) + Character
                        .getNumericValue(b.charAt(b_len - 1 - i));
            } else if (i >= a_len) {
                temp = Character.getNumericValue(b.charAt(b_len - 1 - i));
            } else {
                temp = Character.getNumericValue(a.charAt(a_len - 1 - i));
            }

            temp += plus;
            plus = 0;
            if (temp >= 2) {
                plus = 1;
                temp = temp % 2;
            }
            ans = String.valueOf(temp) + ans;
        }
        if (plus == 1) {
            ans = String.valueOf(plus) + ans;
        }

        return String.valueOf(ans);
    }

    public static void main(String[] args) {
        System.out.println();
        AddBinary sol = new AddBinary();
        String a = "1", b = "111";
        System.out.println(sol.addBinary(a, b));
    }
}
