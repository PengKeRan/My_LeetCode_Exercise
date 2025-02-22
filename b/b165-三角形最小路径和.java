import java.util.*;

class MinimumTotal {
    public int minimumTotal(List<List<Integer>> triangle) {
        // List<Integer> dp = new ArrayList<>();
        // dp.add(triangle.get(0).get(0));
        // for (int i = 1; i < triangle.size(); i++) {
        // List<Integer> temp = triangle.get(i);
        // int n = temp.size();
        // for (int j = 0; j < n; j++) {
        // if (j == 0) {
        // dp.add(dp.get(0) + temp.get(j));
        // } else if (j == n - 1) {
        // dp.add(dp.get(0) + temp.get(j));
        // dp.remove(0);
        // } else {
        // dp.add(Math.min(dp.get(0), dp.get(1)) + temp.get(j));
        // dp.remove(0);
        // }
        // }
        // System.out.println(dp);
        // }
        // return Collections.min(dp);

        int n = triangle.size();
        List<Integer> dp = new ArrayList<>(triangle.get(n - 1)); // 初始化为最后一行
        for (int i = n - 2; i >= 0; i--) {
            List<Integer> temp = triangle.get(i);
            for (int j = 0; j < temp.size(); j++) {
                dp.set(j, Math.min(dp.get(j), dp.get(j + 1)) + temp.get(j));
            }
        }
        return dp.get(0);
    }

    public static void main(String[] args) {
        MinimumTotal sol = new MinimumTotal();
        List<List<Integer>> list = new ArrayList<>();
        list.add(new ArrayList<>(Arrays.asList(2)));
        list.add(new ArrayList<>(Arrays.asList(3, 4)));
        list.add(new ArrayList<>(Arrays.asList(6, 5, 7)));
        list.add(new ArrayList<>(Arrays.asList(4, 1, 8, 3)));
        System.out.println(sol.minimumTotal(list));
    }
}