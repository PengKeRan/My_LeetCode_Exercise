// 581. 最短无序连续子数组
// 给你一个整数数组 nums，你需要找出一个 连续子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
// 请你找出符合题意的 最短 子数组，并输出它的长度。

import java.util.*;

class FindUnsortedSubarray {
    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length;
        int left = n - 1, right = 0;
        int min_right = nums[n - 1];
        int max_left = nums[0];

        for (int i = 0; i < n; i++) {
            if (nums[n - 1 - i] <= min_right) {
                min_right = nums[n - 1 - i];
            } else {
                left = n - 1 - i;
            }

            if (nums[i] >= max_left) {
                max_left = nums[i];
            } else {
                right = i;
            }
        }
        return right <= left ? 0 : right - left + 1;
    }

    public static void main(String[] args) {
        FindUnsortedSubarray sol = new FindUnsortedSubarray();
        int[] intervals = { 1, 2, 3, 3, 3 };
        System.out.println(sol.findUnsortedSubarray(intervals));
    }
}
