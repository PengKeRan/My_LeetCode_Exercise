class TrailingZeroes {
    public int trailingZeroes(int n) {
        int fives = 0; // 5 的数量
        int temp = 5;
        while (temp <= n) {
            fives += n / temp;
            temp *= 5;
        }
        return fives;
    }

    public static void main(String[] args) {
        TrailingZeroes sol = new TrailingZeroes();
        System.out.println(sol.trailingZeroes(5));
    }
}
