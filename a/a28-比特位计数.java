class bitsCount {
    public int[] countBits(int n) {
        int[] res = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            System.out.println(i + '-' + res[i >> 1] + '-' + i & 1);
            res[i] = res[i >> 1] + (i & 1);
        }
        return res;
    }
}
