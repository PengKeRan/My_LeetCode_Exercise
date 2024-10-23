// LCR 003. 比特位计数
// 给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。

class CountBits {
    public int[] countBits(int n) {
        int[] ans = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            ans[i] = ans[i >> 1] + (i & 1);
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println();
        CountBits sol = new CountBits();
        int n = 5;
        System.out.println(sol.countBits(n));
    }
}
