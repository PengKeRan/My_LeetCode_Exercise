import java.util.*;

class MaxSubarraySumCircular {
    public int maxSubarraySumCircular(int[] nums) {
        int n = nums.length;
        int maxSum = nums[0];
        int minSum = nums[0];
        int curMaxSum = nums[0];
        int curMinSum = nums[0];
        int sum = nums[0];
        for (int i = 1; i < n; i++) {
            sum += nums[i];
            curMaxSum = Math.max(nums[i], curMaxSum + nums[i]);
            maxSum = Math.max(maxSum, curMaxSum);
            curMinSum = Math.min(nums[i], curMinSum + nums[i]);
            minSum = Math.min(minSum, curMinSum);
        }
        if (sum == minSum) {
            return maxSum;
        } else {
            return Math.max(maxSum, sum - minSum);
        }
    }

    public static void main(String[] args) {
        MaxSubarraySumCircular obj = new MaxSubarraySumCircular();
        int[] nums = { -3, -2, -3 };
        System.out.println(obj.maxSubarraySumCircular(nums));
    }
}
