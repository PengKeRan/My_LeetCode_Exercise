// 347. 前 K 个高频元素
// 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;

class TopKFrequent {
    // public int[] topKFrequent(int[] nums, int k) {
    // Map<String, Integer> memo = new LinkedHashMap<>();
    // for (int i = 0; i < nums.length; i++) {
    // String key = String.valueOf(nums[i]);
    // if (memo.containsKey(key)) {
    // memo.put(key, memo.get(key) + 1);
    // } else {
    // memo.put(key, 1);
    // }
    // }

    // List<Map.Entry<String, Integer>> list = new ArrayList<>(memo.entrySet());

    // // 使用自定义Comparator对List进行排序
    // Collections.sort(list, (o1, o2) -> o2.getValue().compareTo(o1.getValue()));

    // // 取前k个元素
    // int[] result = new int[k];
    // for (int i = 0; i < k; i++) {
    // result[i] = Integer.valueOf(list.get(i).getKey());
    // }

    // return result;
    // }

    // 堆排序
    // public int[] topKFrequent(int[] nums, int k) {
    // Map<Integer, Integer> memo = new HashMap<>();
    // for (int i = 0; i < nums.length; i++) {
    // memo.put(nums[i], memo.getOrDefault(nums[i], 0) + 1);
    // }

    // List<Map.Entry<Integer, Integer>> list = new ArrayList<>(memo.entrySet());
    // int n = list.size();

    // for (int i = n - 1; i >= 0; i--) {
    // for (int j = (i + 1 / 2) - 1; j >= 0; j--) {
    // upFilter(list, j, i + 1);
    // }
    // exchange(list, 0, i);
    // }

    // // 取前k个元素
    // int[] result = new int[k];
    // for (int i = 0; i < k; i++) {
    // result[i] = Integer.valueOf(list.get(i).getKey());
    // }

    // return result;
    // }

    // public void upFilter(List<Map.Entry<Integer, Integer>> list, int i, int n) {
    // int temp = i;
    // if (2 * i + 1 < n && list.get(i).getValue() > list.get(2 * i +
    // 1).getValue()) {
    // temp = 2 * i + 1;
    // }
    // if (2 * i + 2 < n && list.get(temp).getValue() > list.get(2 * i +
    // 2).getValue()) {
    // temp = 2 * i + 2;
    // }
    // if (i != temp) {
    // exchange(list, i, temp);
    // }
    // }

    // public void exchange(List<Map.Entry<Integer, Integer>> list, int i, int j) {
    // Map.Entry<Integer, Integer> temp = list.get(i);
    // list.set(i, list.get(j));
    // list.set(j, temp);
    // }

    // 桶排序
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> memo = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            memo.put(nums[i], memo.getOrDefault(nums[i], 0) + 1);
        }

        List<Integer>[] buckets = new List[nums.length + 1];
        for (Integer key : memo.keySet()) {
            if (buckets[memo.get(key)] == null) {
                buckets[memo.get(key)] = new ArrayList();
            }
            buckets[memo.get(key)].add(key);
        }

        int[] res = new int[k];
        int pos = 0;
        for (int i = nums.length; i >= 0 && pos < k; i--) {
            if (buckets[i] != null) {
                for (int j = 0; j < buckets[i].size(); j++) {
                    res[pos] = buckets[i].get(j);
                    pos++;
                }
            }
        }

        return res;
    }

    public static void main(String[] args) {
        TopKFrequent sol = new TopKFrequent();
        int[] nums1 = { 1 };
        int k1 = 1;
        System.out.println(sol.topKFrequent(nums1, k1));
        // System.out.println(sol.decodeString(s2));
    }
}
