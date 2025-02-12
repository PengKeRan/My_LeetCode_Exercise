class SearchRange {
    public int[] searchRange(int[] nums, int target) {
        int left = sideSearch(nums, target, true);
        int right = sideSearch(nums, target, false) - 1;
        if (left <= right && left >= 0 && right < nums.length && nums[left] == target && nums[right] == target) {
            return new int[] { left, right };
        }
        return new int[] { -1, -1 };
    }

    private int sideSearch(int[] nums, int target, boolean flag) {
        int ans = nums.length;
        int left = 0, right = nums.length - 1;
        int mid;
        while (left <= right) {
            mid = (left + right) / 2;
            if (flag) {
                if (nums[mid] < target) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                    ans = mid;
                }
            } else {
                if (nums[mid] <= target) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                    ans = mid;
                }
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] nums = { 8, 8 };
        SearchRange sol = new SearchRange();
        int[] res = sol.searchRange(nums, 8);
        System.out.println(res[0] + "," + res[1]);
    }
}
