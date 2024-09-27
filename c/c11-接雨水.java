// 42. 接雨水
// 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Trap {

    public int trap(int[] height) {
        // 单调栈
        int n = height.length;
        int res = 0;
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            while (!stack.empty() && height[stack.peek()] <= height[i]) {
                int top = stack.pop();
                if (stack.empty()) {
                    break;
                }
                int left = stack.peek();
                int wid = i - left - 1;
                int hei = Math.min(height[i], height[left]) - height[top];
                res += wid * hei;
            }
            stack.push(i);
        }
        return res;
        // 双指针
        // int n = height.length;
        // int left = 0, right = n - 1;
        // int res = 0;
        // int h = Math.min(height[left], height[right]);
        // while (left < right) {
        // if (height[left] <= height[right]) {
        // left++;
        // } else {
        // right--;
        // }
        // h = Math.max(h, Math.min(height[left], height[right]));
        // if (height[left] < h) {
        // res += h - height[left];
        // }
        // if (height[right] < h) {
        // res += h - height[right];
        // }
        // }
        // return res;
    }

    public static void main(String[] args) {
        Trap sol = new Trap();
        int[] height = { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
        System.out.println(sol.trap(height));
    }
}
