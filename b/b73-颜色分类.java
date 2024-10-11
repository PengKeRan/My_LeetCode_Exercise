// 75. 颜色分类
// 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
// 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
// 必须在不使用库内置的 sort 函数的情况下解决这个问题。

import java.util.*;

class SortColors {
    public void sortColors(int[] nums) {
        int n = nums.length;
        int left = 0, right = n - 1;
        int i = 0;
        while (i <= right) {
            if (left > i) {
                if (i > right) {
                    return;
                }
                i = left;
            }
            if (nums[i] == 0) {
                swap(nums, i, left);
                left++;
            }
            if (nums[i] == 2) {
                swap(nums, i, right);
                right--;
            }
            if (nums[i] == 1) {
                i++;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        System.out.println("swap:" + i + "-" + j);
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public static void main(String[] args) {
        SortColors sol = new SortColors();
        int[] nums = { 2, 0, 2, 1, 1, 0 };
        sol.sortColors(nums);
        for (Integer num : nums) {
            System.out.print(num);
            System.out.print(",");
        }
    }
}
