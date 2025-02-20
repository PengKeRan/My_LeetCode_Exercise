class IsPalindrome {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        int temp = 0;
        while (temp < x) {
            temp = temp * 10 + x % 10;
            x = x / 10;
        }
        return x == (temp / 10) || x == temp;
    }

    public static void main(String[] args) {
        IsPalindrome sol = new IsPalindrome();
        System.out.println(sol.isPalindrome(10));
    }
}
