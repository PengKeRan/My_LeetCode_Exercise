class MaxPoints {
    public int maxPoints(int[][] points) {
        int n = points.length;
        int ans = 1;
        int cnt = 1;
        int i, j, k;
        int[] p1 = new int[2];
        int[] p2 = new int[2];
        int[] p3 = new int[2];
        for (i = 0; i < n - 1; i++) {
            p1 = points[i];
            for (j = i + 1; j < n; j++) {
                cnt = 2;
                p2 = points[j];
                for (k = j + 1; k < n; k++) {
                    p3 = points[k];
                    if ((p1[1] - p3[1]) * (p2[0] - p3[0]) == (p2[1] - p3[1]) * (p1[0] - p3[0])) {
                        cnt += 1;
                    }
                }
                ans = Math.max(ans, cnt);
            }
        }
        return ans;
    }
}