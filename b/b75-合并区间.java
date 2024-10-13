// 56. 合并区间
// 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
// 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

class Merge {
    public int[][] merge(int[][] intervals) {
        return intervals;
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