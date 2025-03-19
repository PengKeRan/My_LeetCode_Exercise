import java.util.*;

class Solution {
    private List<List<Integer>> res;

    public List<List<Integer>> permute(int[] nums) {
        res = new ArrayList<>();
        List<Integer> new_nums = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            new_nums.add(nums[i]);
        }
        bfs(new_nums, new ArrayList<>());
        return res;
    }

    private void bfs(List<Integer> nums, List<Integer> seq) {
        if (nums.size() == 0) {
            res.add(new ArrayList<>(seq));
        }
        int temp = 0;
        for (int i = 0; i < nums.size(); i++) {
            temp = nums.get(i);

            seq.add(nums.get(i));
            nums.remove(i);
            bfs(nums, seq);
            nums.add(i, temp);
            seq.remove(seq.size() - 1);
        }
    }
}