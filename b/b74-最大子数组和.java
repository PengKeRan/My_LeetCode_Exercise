
// 53. 最大子数组和
// 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
// 子数组是数组中的一个连续部分。

import java.util.*;

class MaxSubArray {
    public int maxSubArray(int[] nums) {
        // // 前缀和
        // int ans = Integer.MIN_VALUE;
        // int n = nums.length;
        // List<Integer> prefixSum = new ArrayList<>();
        // prefixSum.add(nums[0]);

        // for (int i = 1; i < n; i++) {
        // prefixSum.add(prefixSum.get(i - 1) + nums[i]);
        // }

        // for (int i = 0; i < n; i++) {
        // ans = Math.max(ans, prefixSum.get(i));
        // for (int j = 0; j < i; j++) {
        // ans = Math.max(ans, prefixSum.get(i) - prefixSum.get(j));
        // }
        // }

        // return ans;

        // 动态规划
        // int n = nums.length;
        // int[][] dp = new int[2][n];

        // dp[0][0] = Integer.MIN_VALUE;
        // dp[1][0] = nums[0];

        // for (int i = 1; i < n; i++) {
        // dp[0][i] = Math.max(dp[0][i - 1], dp[1][i - 1]);
        // dp[1][i] = Math.max(dp[1][i - 1] + nums[i], nums[i]);
        // }

        // return Math.max(dp[0][n - 1], dp[1][n - 1]);

        // 动态规划2
        int n = nums.length;

        int pre = 0;
        int ans = nums[0];

        for (int i = 0; i < n; i++) {
            pre = Math.max(nums[i], pre + nums[i]);
            ans = Math.max(ans, pre);
        }

        return ans;

        // 精妙的分治法
        // return getInfo(nums, 0, nums.length - 1).mSum;
    }

    class Status {
        int lSum, rSum, mSum, iSum;

        Status(int lSum, int rSum, int mSum, int iSum) {
            this.lSum = lSum; // 包含左端点
            this.rSum = rSum; // 包含右端点
            this.mSum = mSum; // 最大的
            this.iSum = iSum; // 都包含
        }

    }

    private Status getInfo(int[] nums, int left, int right) {
        if (left == right) {
            return new Status(nums[left], nums[left], nums[left], nums[left]);
        }
        int mid = (right + left) / 2;
        System.out.println(mid);
        Status sLeft = getInfo(nums, left, mid);
        Status sRight = getInfo(nums, mid + 1, right);

        int iSum = sLeft.iSum + sRight.iSum;
        int lSum = Math.max(sLeft.lSum, sLeft.iSum + sRight.lSum);
        int rSum = Math.max(sRight.rSum, sRight.iSum + sLeft.rSum);
        int mSum = Math.max(Math.max(sLeft.mSum, sRight.mSum), sLeft.rSum + sRight.lSum);

        return new Status(lSum, rSum, mSum, iSum);
    }

    // private Status calStatus(Status left, Status right) {
    // return null;
    // }

    public static void main(String[] args) {
        MaxSubArray sol = new MaxSubArray();
        int[] nums = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        System.out.println(sol.maxSubArray(nums));
    }
}