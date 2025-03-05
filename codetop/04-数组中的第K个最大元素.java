class Solution {
    public int findKthLargest(int[] nums, int k) {
        heapSort(nums);
        return nums[k - 1];
    }

    private void heapSort(int[] nums) {
        int n = nums.length;
        for (int i = n - 1; i >= 0; i--) {
            downFilter(nums, i, n);
        }
        for (int i = n - 1; i >= 0; i--) {
            swap(nums, 0, i);
            downFilter(nums, 0, i);
        }
    }

    private void downFilter(int[] nums, int i, int n) {
        int temp = i;
        int left = 2 * i + 1;
        int right = left + 1;
        if (left < n && nums[left] < nums[temp]) {
            temp = left;
        }
        if (right < n && nums[right] < nums[temp]) {
            temp = right;
        }
        if (temp != i) {
            swap(nums, i, temp);
            downFilter(nums, temp, n);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}