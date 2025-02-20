class MyPow {
    public double myPow(double x, int n) {
        if (x == 1) {
            return 1;
        }
        if (n == 0) {
            return 1;
        }
        long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }

        double res = 1;
        while (N > 0) {
            if (N % 2 == 1) {
                res *= x;
            }
            x *= x;
            N /= 2;
        }
        return res;

        // double res = x;
        // int temp = 1;
        // double nn = N;
        // while (N > 1 && n % 2 == 0) {
        // res = res * res;
        // N = N / 2;
        // temp *= 2;
        // }
        // for (double more = nn - temp; more > 0; more--) {
        // res = res * x;
        // }
        // return res;
    }

    public static void main(String[] args) {
        MyPow sol = new MyPow();
        System.out.println(sol.myPow(2, 3));
    }
}