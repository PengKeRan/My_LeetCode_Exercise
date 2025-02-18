import java.util.*;

class FindMaximizedCapital {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;
        List<int[]> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            arr.add(new int[] { capital[i], profits[i] });
        }
        Collections.sort(arr, (a, b) -> a[0] - b[0]);

        int pos = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        while (k > 0) {
            for (; pos < n && arr.get(pos)[0] <= w; pos++) {
                pq.add(arr.get(pos)[1]);
            }
            if (pq.isEmpty()) {
                return w;
            }
            w += pq.poll();
            k -= 1;
        }
        return w;
    }
}