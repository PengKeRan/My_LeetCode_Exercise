// LCR 132. 砍竹子 II
// 现需要将一根长为正整数 bamboo_len 的竹子砍为若干段，每段长度均为 正整数。请返回每段竹子长度的 最大乘积 是多少。
// 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

import java.util.*;

class CuttingBamboo {
    public int cuttingBamboo(int bamboo_len) {
        if (bamboo_len <= 2) {
            return 1;
        }
        if (bamboo_len == 3) {
            return 2;
        }
        if (bamboo_len == 4) {
            return 4;
        }
        int p = 1000000007;
        return (int) (dp(bamboo_len - 3) * 3 % p);
    }

    private long dp(int n) {
        int p = 1000000007;
        if (n <= 4) {
            return n;
        }
        return dp(n - 3) * 3 % p;
    }

    public static void main(String[] args) {
        CuttingBamboo sol = new CuttingBamboo();
        int n = 120;
        System.out.println(sol.cuttingBamboo(n));
    }
}
