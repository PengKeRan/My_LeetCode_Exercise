// LCR 006. 两数之和 II-输入有序数组 
// 给定一个已按照 升序排列 的整数数组 numbers，请你从数组中找出两个数满足相加之和等于目标数 target。
// 函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 0 开始计数，所以答案数组应当满足 0<=answer[0]<answer[1]<numbers.length。
// 假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。

import java.util.*;

class TwoSum {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length - 1;
        while (left < right) {
            if (numbers[left] + numbers[right] == target) {
                return new int[] { left, right };
            }
            if (numbers[left] + numbers[right] < target) {
                left++;
            } else {
                right--;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        TwoSum sol = new TwoSum();
        int[] numbers = { 1, 2, 4, 6, 10 };
        int target = 8;
        System.out.println(sol.twoSum(numbers, target));
    }
}
