import java.util.ArrayList;
import java.util.List;

class Permute {
    private List<List<Integer>> ans = new ArrayList<>();

    public List<List<Integer>> permute(int[] nums) {
        int n = nums.length;
        List<Integer> output = new ArrayList<Integer>();
        for (int num : nums) {
            output.add(num);
        }
        generate(output, n, 0);
        return ans;
    }

    private void generate(List<Integer> nums, int n, int first) {
        if (first == n) {
            ans.add(new ArrayList<Integer>(nums));
        }
        for (int j = first; j < n; j++) {
            swap(nums, first, j);
            generate(nums, n, first + 1);
            swap(nums, j, first);
        }
    }

    private void swap(List<Integer> nums, int i, int j) {
        int temp = nums.get(i);
        nums.set(i, nums.get(j));
        nums.set(j, temp);
    }

    public static void main(String[] args) {
        Permute sol = new Permute();
        int[] nums = { 1, 2, 3 };
        List<List<Integer>> res = sol.permute(nums);
        for (List<Integer> r : res) {
            System.out.println(String.valueOf(r));
        }
    }
}
