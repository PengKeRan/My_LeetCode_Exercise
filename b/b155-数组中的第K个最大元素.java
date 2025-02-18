class FindKthLargest {
    public int findKthLargest(int[] nums, int k) {
        int n = nums.length;
        for (int i = n - 1; i >= 0; i--) {
            downFilter(nums, n, i);
        }
        for (int i = n - 1; i >= 0; i--) {
            swap(nums, 0, i);
            downFilter(nums, i, 0);
        }
        return nums[k - 1];
    }

    private void downFilter(int[] nums, int n, int i) {
        int left = 2 * i + 1;
        int right = left + 1;
        int temp = i;
        if (left < n && nums[left] < nums[temp]) {
            temp = left;
        }
        if (right < n && nums[right] < nums[temp]) {
            temp = right;
        }
        if (temp != i) {
            swap(nums, i, temp);
            downFilter(nums, n, temp);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public static void main(String[] args) {
        int[] nums = { 3, 2, 1, 5, 6, 4 };
        FindKthLargest sol = new FindKthLargest();
        System.out.println(sol.findKthLargest(nums, 2));
    }
}