// 32. 最长有效括号
// 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Solution {
    public int longestValidParentheses(String s) {
        // int ans = 0;
        // int n = s.length();
        // int curLen = 0;
        // Stack<Integer> stack = new Stack<>();
        // stack.push(-1);
        // for (int i = 0; i < n; i++) {
        // char ch = s.charAt(i);
        // if (ch == '(') {
        // stack.push(i);
        // } else {
        // if (!stack.isEmpty() && stack.peek() == '(') {
        // stack.pop();
        // curLen += 2;
        // ans = Math.max(ans, curLen);
        // } else {
        // stack.pop();
        // if (stack.isEmpty()) {
        // stack.push(i);
        // } else {
        // ans = Math.max(ans, i - stack.peek());
        // }
        // }
        // }
        // }
        // return ans;

        int left = 0, right = 0;
        int n = s.length();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if (ch == '(') {
                left += 1;
            } else {
                right++;
            }
            if (right > left) {
                left = 0;
                right = 0;
            }
            if (left == right) {
                ans = Math.max(ans, left + right);
            }
        }
        left = 0;
        right = 0;
        for (int i = n - 1; i >= 0; i--) {
            char ch = s.charAt(i);
            if (ch == '(') {
                left += 1;
            } else {
                right++;
            }
            if (right < left) {
                left = 0;
                right = 0;
            }
            if (left == right) {
                ans = Math.max(ans, left + right);
            }
        }
        return ans;

    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String s = "())";
        System.out.println(sol.longestValidParentheses(s));
    }
}
