class ReverseBits {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int res = 0;
        int i = 0;
        while (i < 32) {
            res = (res << 1) | (n & 1);
            n = n >>> 1;
            i += 1;
        }
        return 0;
    }
}