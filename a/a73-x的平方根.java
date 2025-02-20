class MySqrt {
    public int mySqrt(int x) {
        // if (x == 0) {
        // return 0;
        // }
        // int res = 1;
        // while (res <= x / res) {
        // res += 1;
        // }
        // return res - 1;
        // 二分
        int l = 0, r = x, ans = -1;
        int mid = 0;
        while (l <= r) {
            mid = (l + r) / 2;
            if ((long) mid * mid <= x) {
                l = mid + 1;
                ans = mid;
            } else {
                r = mid - 1;
            }
        }
        return ans;
    }
}