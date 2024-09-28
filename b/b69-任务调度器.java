// 621. 任务调度器
// 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表，用字母 A 到 Z 表示，以及一个冷却时间 n。
// 每个周期或时间间隔允许完成一项任务。任务可以按任何顺序完成，但有一个限制：两个 相同种类 的任务之间必须有长度为 n 的冷却时间。
// 返回完成所有任务所需要的 最短时间间隔。

import java.util.Arrays;

class LeastInterval {
    public int leastInterval(char[] tasks, int n) {
        int[] hash = new int[26];
        for (int i = 0; i < tasks.length; i++)
            hash[tasks[i] - 'A'] += 1;
        Arrays.sort(hash);
        int minlen = (n + 1) * (hash[25] - 1) + 1;
        for (int i = 0; i < 25; i++)
            if (hash[i] == hash[25])
                minlen++;

        return Math.max(tasks.length, minlen);
    }

    public static void main(String[] args) {
        LeastInterval sol = new LeastInterval();
        char[] tasks = { 'A', 'A', 'A', 'B', 'B', 'B' };
        int n = 2;
        System.out.println(sol.leastInterval(tasks, n));
    }
}
