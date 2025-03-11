import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> memo = new HashMap<>();
        int[] res = new int[2];
        for (int i = 0; i < nums.length; i++) {
            int val = nums[i];
            if (memo.containsKey(target - val)) {
                res[0] = memo.get(target - val);
                res[1] = i;
                return res;
            } else {
                if (!memo.containsKey(val)) {
                    memo.put(val, i);
                }
            }
        }
        return res;
    }
}