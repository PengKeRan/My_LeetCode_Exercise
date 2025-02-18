import java.util.*;

class KSmallestPairs {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        int n1 = nums1.length;
        int n2 = nums2.length;
        List<List<Integer>> res = new ArrayList<>();
        PriorityQueue<List<Integer>> pq = new PriorityQueue<>((a, b) -> nums1[a
                .get(0)] + nums2[a.get(1)] - nums1[b.get(0)] - nums2[b.get(1)]);
        for (int i = 0; i < k && i < n1; i++) {
            pq.add(Arrays.asList(i, 0));
        }
        while (k > 0 && !pq.isEmpty()) {
            List<Integer> top = pq.poll();
            res.add(Arrays.asList(nums1[top.get(0)], nums2[top.get(1)]));
            k -= 1;
            if (top.get(1) < n2 - 1) {
                pq.add(Arrays.asList(top.get(0), top.get(1) + 1));
            }
        }
        return res;
    }
}