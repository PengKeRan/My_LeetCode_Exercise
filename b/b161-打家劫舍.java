import java.util.*;

class Rob {
    public int rob(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        res[0] = nums[0];
        if (n > 1) {
            res[1] = Math.max(res[0], nums[1]);
        }
        for (int i = 2; i < n; i++) {
            res[i] = Math.max(res[i - 1], res[i - 2] + nums[i]);
        }

        return res[n - 1];
    }
}