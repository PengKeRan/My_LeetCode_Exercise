class Solution {
    public void moveZeroes(int[] nums) {
        // int j = 0;
        // for (int i = 0; i < nums.length; i++) {
        // if (j >= nums.length) {
        // return;
        // }
        // if (nums[i] == 0) {
        // while (nums[j] == 0) {
        // j += 1;
        // }
        // exchange(nums, i, j);
        // j += 1;
        // }
        // }
        int left = 0, right = 0;
        while (right < nums.length) {
            if (nums[right] != 0) {
                exchange(nums, left, right);
                left += 1;
            }
            right += 1;
        }
    }

    public static void exchange(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        return;
    }
}