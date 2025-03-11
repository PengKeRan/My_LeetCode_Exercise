import java.util.*;

class Ssearch {
    public int search(int[] nums, int target) {
        return findPart(nums, 0, nums.length - 1, target);
    }

    private int findPart(int[] nums, int left, int right, int target) {
        if (left > right || (left == right && nums[left] != target)) {
            return -1;
        }
        int mid = (left + right) / 2;
        if (nums[mid] >= nums[left]) {
            if (nums[left] <= target && target <= nums[mid]) {
                return binarySearch(nums, left, mid, target);
            } else {
                return findPart(nums, mid + 1, right, target);
            }
        } else {
            if (nums[mid] <= target && target <= nums[right]) {
                return binarySearch(nums, mid, right, target);
            } else {
                return findPart(nums, left, mid - 1, target);
            }
        }
    }

    private int binarySearch(int[] nums, int left, int right, int target) {
        int mid, l = left, r = right;
        while (l < r) {
            mid = (l + r) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        if (nums[l] != target) {
            return -1;
        } else {
            return l;
        }
    }

    public static void main(String[] args) {
        int[] nums = { 1, 3, 5 };
        int target = 2;
        Ssearch sol = new Ssearch();
        System.out.println(sol.search(nums, target));
    }
}