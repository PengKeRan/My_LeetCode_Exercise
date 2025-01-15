import java.util.List;
import java.util.ArrayList;

class CombinationSum {
    List<List<Integer>> result;
    int target;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        this.result = new ArrayList<>();
        this.target = target;
        bfs(candidates, 0, new ArrayList<>(), 0);
        return this.result;
    }

    private void bfs(int[] nums, int start, List<Integer> seq, int total) {
        for (int i = start; i < nums.length; i++) {
            if (total >= this.target) {
                if (total == this.target) {
                    this.result.add(new ArrayList<>(seq));
                }
                return;
            }
            seq.add(nums[i]);
            bfs(nums, i, seq, total + nums[i]);
            seq.remove(seq.size() - 1);
        }
    }

    public static void main(String[] args) {
        int[] nums = { 2, 3, 6, 7 };
        int target = 7;
        CombinationSum sol = new CombinationSum();
        System.err.println(sol.combinationSum(nums, target));
    }
}
