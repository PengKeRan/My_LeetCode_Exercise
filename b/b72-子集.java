
// 78. 子集
// 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
// 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
import java.util.*;

class Subsets {
    public List<List<Integer>> subsets(int[] nums) {
        int n = nums.length;
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        int mask = 0;
        int i;
        for (; mask < (1 << n); mask++) {
            temp.clear();
            for (i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    temp.add(nums[i]);
                }
            }
            ans.add(new ArrayList<>(temp));
        }
        return ans;
    }

    public static void main(String[] args) {
        Subsets sol = new Subsets();
        int[] nums1 = { 1, 2, 3 };
        System.out.println(sol.subsets(nums1));
    }
}