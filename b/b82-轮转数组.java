// 189. 轮转数组
// 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

class Rotate2 {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;
        int[] tempArr = new int[k];
        int i, j;
        if (n == 1) {
            return;
        }
        for (i = 0; i < k; i++) {
            tempArr[i] = nums[n - k + i];
        }
        for (j = n - 1; j >= k; j--) {
            nums[j] = nums[j - k];
        }
        for (i = 0; i < k; i++) {
            nums[i] = tempArr[i];
        }
    }

    public static void main(String[] args) {
        Rotate2 sol = new Rotate2();
        int[] nums = { 1, 2, 3, 4, 5, 6, 7 };
        int k = 3;
        sol.rotate(nums, k);
        System.out.println(1);
    }
}
