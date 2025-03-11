import java.util.Arrays;
import java.util.Random;

class SortArray {
    public int[] sortArray(int[] nums) {
        int n = nums.length;
        quickSort(nums, 0, n - 1);
        return nums;
    }

    private void quickSort(int[] nums, int left, int right) {
        if (left >= right) {
            return;
        }
        int idx = new Random().nextInt(right - left + 1) + left;
        swap(nums, left, idx);
        int val = nums[left];
        int l = left + 1, r = right;
        while (l <= r) {
            if (nums[l] < val) {
                l++;
            } else if (nums[r] > val) {
                r--;
            } else {
                swap(nums, l, r);
                l++;
                r--;
            }
        }
        swap(nums, left, r);
        quickSort(nums, left, r - 1);
        quickSort(nums, r + 1, right);
    }

    private void swap(int[] nums, int i, int j) {
        if (i != j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }

    public static void main(String[] args) {
        int[] nums = { 5, 2, 3, 1 };
        SortArray sol = new SortArray();
        sol.sortArray(nums);
        System.out.println("排序后的数组: " + Arrays.toString(nums));
    }
}