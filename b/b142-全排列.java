import java.util.List;
import java.util.ArrayList;

class Permute {
    List<List<Integer>> result;

    public List<List<Integer>> permute(int[] nums) {
        this.result = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        for (int num : nums) {
            list.add(num); // 自动拆箱 int -> Integer
        }
        bfs(list, new ArrayList<>());
        return this.result;
    }

    private void bfs(List<Integer> nums, List<Integer> seq) {
        if (nums.size() == 0) {
            this.result.add(new ArrayList<>(seq));
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            seq.add(nums.get(i));
            nums.remove(i);
            bfs(nums, seq);
            nums.add(i, seq.get(seq.size() - 1));
            seq.remove(seq.size() - 1);
        }
    }

    public static void main(String[] args) {
        int[] nums = { 1, 2, 3 };
        Permute sol = new Permute();
        System.err.println(sol.permute(nums));
    }
}