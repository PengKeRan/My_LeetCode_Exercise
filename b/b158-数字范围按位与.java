class RangeBitwiseAnd {
    public int rangeBitwiseAnd(int left, int right) {
        if (left == right) {
            return left;
        }
        int cnt = 0;
        while (left != right) {
            left = left >> 1;
            right = right >> 1;
            cnt += 1;
        }
        while (cnt > 0) {
            left = left << 1;
            cnt -= 1;
        }
        return left;
    }
}