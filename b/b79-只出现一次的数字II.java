// LCR 004. 只出现一次的数字 II
// 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
class SingleNumber {
    public int singleNumber(int[] nums) {
        int a = 0, b = 0;
        for (int num : nums) {
            int aNext = (~a & b & num) | (a & ~b & ~num), bNext = ~a & (b ^ num);
            a = aNext;
            b = bNext;
        }
        return b;
    }

    public static void main(String[] args) {
        SingleNumber sol = new SingleNumber();
        int[] n = { 2, 2, 3, 2 };
        System.out.println(sol.singleNumber(n));
    }
}
