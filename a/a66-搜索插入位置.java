class SearchInsert {
    public int searchInsert(int[] nums, int target) {
        // int n = nums.length;
        // int left = -1, right = n;

        // while (true) {
        // int mid = (left + right) / 2;
        // if (left == mid) {
        // return left + 1;
        // }
        // if (right == mid) {
        // return right;
        // }
        // if (nums[mid] == target) {
        // return mid;
        // } else if (nums[mid] < target) {
        // left = mid;
        // } else {
        // right = mid;
        // }
        // }
        int n = nums.length;
        int left = 0, right = n - 1;
        int mid;
        while (left <= right) {
            mid = (left + right) / 2;
            if (target <= nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}