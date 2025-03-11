import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        // Set<List<Integer>> result = new HashSet<>();
        List<Integer> temp;

        Arrays.sort(nums);
        int n = nums.length;
        int target, left, right, sum_two;
        for (int i = 0; i < n - 2; i++) {
            if (i >= 1 && nums[i] == nums[i - 1]) {
                continue;
            }
            target = -nums[i];
            left = i + 1;
            right = n - 1;
            while (left < right) {
                sum_two = nums[left] + nums[right];
                if (sum_two == target) {
                    temp = new ArrayList<>();
                    temp.add(-target);
                    temp.add(nums[left]);
                    temp.add(nums[right]);
                    res.add(temp);
                    left += 1;
                    while (left < right && nums[left] == nums[left - 1]) {
                        left += 1;
                    }
                } else if (sum_two < target) {
                    left += 1;
                    while (left < right && nums[left] == nums[left - 1]) {
                        left += 1;
                    }
                } else {
                    right -= 1;
                    while (left < right && nums[right] == nums[right + 1]) {
                        right -= 1;
                    }
                }
            }
        }

        return res;
    }

    public static void main(String[] args) {
        int[] nums = { 0, 0, 0, 0 };
        ThreeSum sol = new ThreeSum();
        sol.threeSum(nums);
    }
}