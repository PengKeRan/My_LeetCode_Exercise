import java.util.ArrayList;
import java.util.Scanner;

public class ScannerPractice {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int k = -1;
        ArrayList<Integer> nums = new ArrayList<>();

        while (scan.hasNextLine()) {
            String line = scan.nextLine();
            if (line.equalsIgnoreCase("q")) {
                break; // 输入 'q' 结束循环
            }
            if (line.length() == 1) {
                k = Integer.valueOf(line);
            } else {
                for (int j = 0; j < line.length(); j++) {
                    if (line.charAt(j) != ' ') {
                        nums.add(Character.getNumericValue(line.charAt(j)));
                    }
                }
            }
        }
        int a = 0;
    }
}
