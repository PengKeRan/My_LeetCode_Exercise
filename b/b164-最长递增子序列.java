class LengthOfLIS {
    public int lengthOfLIS(int[] nums) {
        // 动态规划
        // int n = nums.length;
        // int[] res = new int[n];
        // int ans = 1;
        // for (int i = 0; i < n; i++) {
        // res[i] = 1;
        // for (int j = i - 1; j >= 0; j--) {
        // if (nums[i] <= nums[j]) {
        // continue;
        // }
        // res[i] = Math.max(res[i], res[j] + 1);
        // }
        // ans = Math.max(ans, res[i]);
        // }
        // return ans;

        // 二分查找
        int n = nums.length;
        int ans = 0;
        int[] last = new int[n];
        for (int i = 0; i < n; i++) {
            int left = 0, right = ans;
            while (left < right) {
                int mid = (left + right) / 2;
                if (last[mid] < nums[i]) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            last[left] = nums[i];
            if (ans == right) {
                ans++;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] nums = new int[] { 1, 3, 6, 7, 9, 4, 10, 5, 6 };
        LengthOfLIS sol = new LengthOfLIS();
        System.out.println(sol.lengthOfLIS(nums));
    }
}