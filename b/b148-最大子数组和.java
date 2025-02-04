import java.util.*;

class MaxSubArray {
    public int maxSubArray(int[] nums) {
        int result = nums[0];
        int curSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            curSum = Math.max(curSum, curSum + nums[i]);
            result = Math.max(curSum, result);
        }
        return result;
    }
}