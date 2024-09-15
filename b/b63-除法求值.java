// 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和
// values[i] 共同表示
// 等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。
// 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj =
// ? 的结果作为答案。
// 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，
// 也需要用 -1.0 替代这个答案。
// 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。
// 注意：未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Arrays;

class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        int equations_len = equations.size();
        UnionFind unionFind = new UnionFind(equations_len * 2);
        Map<String, Integer> hashmap = new HashMap<>(equations_len * 2);

        int id = 0;
        for (int i = 0; i < equations_len; i++) {
            String x = equations.get(i).get(0);
            String y = equations.get(i).get(1);
            if (!hashmap.containsKey(x)) {
                hashmap.put(x, id);
                id++;
            }
            if (!hashmap.containsKey(y)) {
                hashmap.put(y, id);
                id++;
            }
            unionFind.union(hashmap.get(x), hashmap.get(y), values[i]);
        }

        int queries_len = queries.size();
        double[] res = new double[queries_len];
        for (int i = 0; i < queries_len; i++) {
            String x = queries.get(i).get(0);
            String y = queries.get(i).get(1);
            if (hashmap.containsKey(x) && hashmap.containsKey(y)) {
                res[i] = unionFind.connect(hashmap.get(x), hashmap.get(y));
            } else {
                res[i] = -1.0d;
            }
        }
        unionFind.printInfo();
        return res;
    }

    public class UnionFind {
        private int[] parent;
        private double[] weight;

        public UnionFind(int n) {
            this.parent = new int[n];
            this.weight = new double[n];
            for (int i = 0; i < n; i++) {
                this.parent[i] = i;
                this.weight[i] = 1.0;
            }
        }

        public void union(int x, int y, double value) {
            int parent_x = find(x);
            int parent_y = find(y);

            if (parent_x == parent_y) {
                return;
            }
            parent[parent_x] = parent_y;
            weight[parent_x] = value * weight[y] / weight[x];
        }

        public int find(int x) {
            if (x != parent[x]) {
                int parent_x = parent[x];
                parent[x] = find(parent_x);
                weight[x] *= weight[parent_x];
            }
            return parent[x];
        }

        public double connect(int x, int y) {
            int parent_x = find(x);
            int parent_y = find(y);
            if (parent_x == parent_y) {
                return weight[x] / weight[y];
            }
            return -1.0d;
        }

        public void printInfo() {
            for (int i = 0; i < parent.length; i++) {
                System.out.println(i + "'s parent:" + parent[i]);
            }
            for (int i = 0; i < weight.length; i++) {
                System.out.println(i + "'s weight:" + weight[i]);
            }
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        List<List<String>> equations = Arrays.asList(
                Arrays.asList("a", "b"),
                Arrays.asList("e", "f"),
                Arrays.asList("b", "e"));
        double[] values = { 3.4, 1.4, 2.3 };
        List<List<String>> queries = Arrays.asList(
                Arrays.asList("a", "f")
        // Arrays.asList("b", "a"),
        // Arrays.asList("a", "e"),
        // Arrays.asList("a", "a"),
        // Arrays.asList("x", "x")
        );

        System.out.println(sol.calcEquation(equations, values, queries));
    }
}
