class SearchMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        // int m = matrix.length, n = matrix[0].length;
        // int x = 0, y = n - 1;
        // while (x < m && y >= 0) {
        // if (matrix[x][y] == target) {
        // return true;
        // }
        // if (matrix[x][y] < target) {
        // x += 1;
        // } else {
        // y -= 1;
        // }
        // }
        // return false;
        int m = matrix.length, n = matrix[0].length;
        int left = 0, right = m * n - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            int val = matrix[mid / n][mid % n];
            if (val < target) {
                left = mid + 1;
            } else if (val > target) {
                right = mid - 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
