// 85. 最大矩形
// 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

import java.util.*;

class MaximalRectangle {
    public int maximalRectangle(char[][] matrix) {
        int ans = 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] leftones = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '0') {
                    leftones[i][j] = 0;
                } else {
                    leftones[i][j] = (j == 0) ? 1 : leftones[i][j - 1] + 1;
                }
            }
        }
        // 逐列寻找最大矩形
        // for (int i = 0; i < m; i++) {
        // for (int j = 0; j < n; j++) {
        // if (leftones[i][j] == 0) {
        // continue;
        // }
        // int width = leftones[i][j];
        // int area = width;
        // for (int k = 1; k <= i; k++) {
        // if (leftones[i - k][j] == 0) {
        // break;
        // }
        // width = Math.min(width, leftones[i - k][j]);
        // area = Math.max(area, width * (k + 1));
        // }
        // ans = Math.max(ans, area);

        // }
        // }

        // 单调栈
        for (int j = 0; j < n; j++) {
            int[] left_res = new int[m];
            Arrays.fill(left_res, -1);
            int[] right_res = new int[m];
            Arrays.fill(right_res, m);
            Stack<Integer> stack = new Stack<>();
            for (int i = 0; i < m; i++) {
                while (!stack.empty() && leftones[stack.peek()][j] >= leftones[i][j]) {
                    right_res[stack.peek()] = i;
                    stack.pop();
                }
                if (!stack.empty()) {
                    left_res[i] = stack.peek();
                } else {
                    left_res[i] = -1;
                }
                stack.push(i);
            }
            for (int i = 0; i < m; i++) {
                ans = Math.max(ans, (right_res[i] - left_res[i] - 1) * leftones[i][j]);
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        MaximalRectangle sol = new MaximalRectangle();
        char[][] matrix = {
                { '1', '0', '1', '0', '0' },
                { '1', '0', '1', '1', '1' },
                { '1', '1', '1', '1', '1' },
                { '1', '0', '0', '1', '0' }
        };
        System.out.println(sol.maximalRectangle(matrix));
    }
}