
// LCR 005. 最大单词长度乘积
// 给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。
// 假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。
import java.util.*;

class MaxProduct {
    public int maxProduct(String[] words) {
        int n = words.length;
        int[] mask = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < words[i].length(); j++) {
                mask[i] |= (1 << words[i].charAt(j) - 'a');
            }
        }
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if ((mask[i] & mask[j]) == 0) {
                    res = Math.max(res, words[i].length() * words[j].length());
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        MaxProduct sol = new MaxProduct();
        String[] words = { "abcw", "baz", "foo", "bar", "fxyz", "abcdef" };
        System.out.println(sol.maxProduct(words));
    }
}
