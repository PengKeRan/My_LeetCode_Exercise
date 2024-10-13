// 56. 合并区间
// 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
// 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

import java.util.*;

class Merge {
    public int[][] merge(int[][] intervals) {
        if (intervals.length == 1) {
            return intervals;
        }
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        int n = intervals.length;

        List<int[]> ans = new ArrayList<int[]>();
        ans.add(intervals[0]);

        for (int i = 1; i < n; i++) {
            if (intervals[i][0] <= ans.get(ans.size() - 1)[1]) {
                ans.get(ans.size() - 1)[1] = Math.max(ans.get(ans.size() - 1)[1], intervals[i][1]);
            } else {
                ans.add(intervals[i]);
            }
        }

        return ans.toArray(new int[ans.size()][]);
        // int[][] ans = new int[n][2];
        // Arrays.fill(ans, 0, n, null);
        // ans[0] = intervals[0];
        // int ans_pos = 1;
        // for (int i = 1; i < n; i++) {
        // if (intervals[i][0] <= ans[ans_pos - 1][1]) {
        // ans[ans_pos - 1][1] = Math.max(ans[ans_pos - 1][1], intervals[i][1]);
        // } else {
        // ans[ans_pos] = intervals[i];
        // ans_pos++;
        // }
        // }
        // return Arrays.copyOfRange(ans, 0, ans_pos);
    }

    public static void main(String[] args) {
        Merge sol = new Merge();
        int[][] intervals = {
                { 1, 3 },
                { 2, 6 },
                { 8, 10 },
                { 15, 18 }
        };
        int[][] res = sol.merge(intervals);
        for (int[] interval : res) {
            System.out.println("[" + interval[0] + ", " + interval[1] + "]");
        }
    }
}