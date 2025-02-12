class FindMin {
    public int findMin(int[] nums) {
        int n = nums.length;
        int left = 0, right = n - 1;
        int mid;
        int ans = nums[0];
        while (left < right) {
            mid = (left + right) / 2;
            if (nums[mid] >= nums[0]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return Math.min(ans, nums[left]);
    }
}