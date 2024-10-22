// LCR 131. 砍竹子 I 
// 现需要将一根长为正整数 bamboo_len 的竹子砍为若干段，每段长度均为正整数。请返回每段竹子长度的最大乘积是多少。

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
        return dp(bamboo_len - 3) * 3;
    }

    private int dp(int n) {
        if (n <= 4) {
            return n;
        }
        return dp(n - 3) * 3;
    }

    public static void main(String[] args) {
        CuttingBamboo sol = new CuttingBamboo();
        int n = 12;
        System.out.println(sol.cuttingBamboo(n));
    }
}
