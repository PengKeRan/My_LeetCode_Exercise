import java.util.*;

class PlusOne {
    public int[] plusOne(int[] digits) {
        List<Integer> res = new ArrayList<>();
        int c = 1;
        int n = digits.length;
        int temp = 0;
        for (int i = n - 1; i >= 0; i--) {
            temp = c + digits[i];
            if (temp >= 10) {
                c = 1;
                res.add(0, temp % 10);
            } else {
                c = 0;
                res.add(0, temp);
            }
        }
        if (c == 1) {
            res.add(0, 1);
        }

        int[] arr = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            arr[i] = res.get(i); // 将 ArrayList 的元素存入 int[] 数组
        }
        return arr;
    }

    public static void main(String[] args) {
        PlusOne sol = new PlusOne();
        System.out.println(sol.plusOne(new int[] { 1, 2, 3 }));
    }
}
