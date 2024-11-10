
// 88. 合并两个有序数组
// 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
// 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
// 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。
// 为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
import java.util.*;

class Merge2 {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int a = m - 1, b = n - 1;
        int i = m + n - 1;
        while (a >= 0 && b >= 0) {
            if (nums1[a] > nums2[b]) {
                nums1[i] = nums1[a];
                a--;
            } else {
                nums1[i] = nums2[b];
                b--;
            }
            i--;
        }
        while (b >= 0) {
            nums1[i] = nums2[b];
            b--;
            i--;
        }
    }

    public static void main(String[] args) {
        Merge2 sol = new Merge2();
        int[] nums1 = { 0 };
        int[] nums2 = { 1 };
        int m = 0, n = 1;
        sol.merge(nums1, m, nums2, n);
    }
}