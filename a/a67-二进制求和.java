class Solution {
    public String addBinary(String a, String b) {
        if (a.length() < b.length()) {
            String temp = a;
            a = b;
            b = temp;
        }
        int n1 = a.length();
        int n2 = b.length();
        boolean c = false;
        StringBuilder res = new StringBuilder();
        int i;
        for (i = 0; i < Math.min(n1, n2); i++) {
            boolean x = a.charAt(n1 - 1 - i) == '1';
            boolean y = b.charAt(n2 - 1 - i) == '1';
            res.append(x ^ y ^ c ? '1' : '0');
            c = (x && y) || ((x ^ y) && c);
        }
        for (; i < n1; i++) {
            boolean x = a.charAt(n1 - 1 - i) == '1';
            res.append(x ^ c ? '1' : '0');
            c = x && c;
        }
        if (c) {
            res.append('1');
        }
        return res.reverse().toString();
    }
}