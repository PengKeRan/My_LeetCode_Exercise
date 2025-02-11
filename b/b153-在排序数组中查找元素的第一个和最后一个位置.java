class SearchRange {
    public int[] searchRange(int[] nums, int target) {
        int n = nums.length;
        if (n == 0) {
            return new int[] { -1, -1 };
        }
        return search(nums, 0, n - 1, target);
    }

    private int[] search(int[] nums, int left, int right, int target) {
        System.out.println(left + "," + right);
        int mid = (left + right) / 2;

        if (left == right) {
            return nums[mid] == target ? new int[] { left, left } : new int[] { -1, -1 };
        }
        if (left + 1 == right) {
            if (nums[left] == target && nums[right] == target) {
                return new int[] { left, right };
            } else if (nums[left] == target) {
                return new int[] { left, left };
            } else if (nums[right] == target) {
                return new int[] { right, right };
            } else {
                return new int[] { -1, -1 };
            }
        }

        if (nums[mid] < target) {
            return search(nums, mid + 1, right, target);
        } else if (nums[mid] > target) {
            return search(nums, left, mid - 1, target);
        } else {
            int[] res = new int[2];
            res[0] = search(nums, left, mid, target)[0];
            res[1] = search(nums, mid, right, target)[1];
            return res;
        }
    }

    public static void main(String[] args) {
        int[] nums = { 5, 7, 7, 8, 8, 10 };
        SearchRange sol = new SearchRange();
        int[] res = sol.searchRange(nums, 8);
        System.out.println(res[0] + "," + res[1]);
    }
}
