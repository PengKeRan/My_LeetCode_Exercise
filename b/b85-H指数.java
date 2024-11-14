// 274. H 指数
// 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。
// 计算并返回该研究者的 h 指数。
// 根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，
// 并且 至少 有 h 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个。

class HIndex {
    public int hIndex(int[] citations) {
        int n = citations.length;
        int[] bucket = new int[n + 1];
        int i;
        for (i = 0; i < n + 1; i++) {
            bucket[i] = 0;
        }
        for (i = 0; i < n; i++) {
            if (citations[i] < n) {
                bucket[citations[i]] += 1;
            } else {
                bucket[n] += 1;
            }
        }
        int temp = 0;
        for (i = n; i >= 0; i--) {
            temp += bucket[i];
            if (temp >= i) {
                return i;
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        HIndex sol = new HIndex();
        int[] citations = { 3, 0, 6, 1, 5 };
        System.out.println(sol.hIndex(citations));
    }
}