class CclimbStairs {
    public int climbStairs(int n) {
        n = n + 1;
        double s5 = Math.sqrt(5);
        return (int) Math.round((1 / s5) * (Math.pow((1 + s5) / 2, n) + Math.pow((s5 - 1) / 2, n)));
    }
}