import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Arrays;
import java.util.Stack;

class DecodeString {
    public String decodeString(String s) {
        int left = findLeft(s);
        if (left == -1) {
            return s;
        }

        int right = findRight(s, left);
        if (right == -1) {
            System.out.println("Error, right = -1 !!");
        }
        String new_s = copySub(left, right, s);
        return decodeString(new_s);
    }

    public int findLeft(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '[') {
                return i;
            }
        }
        return -1;
    }

    public int findRight(String s, int left) {
        int count = 1;
        for (int i = left + 1; i < s.length(); i++) {
            if (s.charAt(i) == '[') {
                count += 1;
            }
            if (s.charAt(i) == ']') {
                count -= 1;
                if (count == 0) {
                    return i;
                }
            }
        }
        return -1;
    }

    public String copySub(int left, int right, String s) {
        // int copyTimes = Character.getNumericValue(s.charAt(left - 1));
        String num_before = getNumber(s, left);
        int copyTimes = Integer.parseInt(num_before);

        String subStr = s.substring(left + 1, right);
        String new_s = s.substring(0, left - num_before.length());
        for (int i = 0; i < copyTimes; i++) {
            new_s += subStr;
        }
        new_s += s.substring(right + 1);
        return new_s;
    }

    public String getNumber(String s, int left) {
        int num_left = left - 1;
        for (int i = left - 2; i >= 0; i--) {
            if (s.charAt(i) >= 65) {
                break;
            } else {
                num_left -= 1;
            }
        }
        return s.substring(num_left, left);
    }

    public String decodeString2(String s) {
        Stack<String> stack = new Stack<>();
        String numRead = "";
        String copyStr = "";
        for (Character ch : s.toCharArray()) {
            if (ch == '[') {
                stack.push(numRead);
                stack.push("[");
                numRead = "";
            }
            if (Character.isLetter(ch)) {
                stack.push(String.valueOf(ch));
            }
            if (Character.isDigit(ch)) {
                numRead += ch;
            }
            if (ch == ']') {
                String topCh = stack.pop();
                while (!topCh.equals("[")) {
                    copyStr = topCh + copyStr;
                    topCh = stack.pop();
                }
                int copyTimes = Integer.parseInt(stack.pop());
                for (int i = 0; i < copyTimes; i++) {
                    stack.push(copyStr);
                }
                copyStr = "";
            }

        }

        String res = "";
        while (!stack.isEmpty()) {
            res = stack.pop() + res;
        }

        return res;
    }

    public static void main(String[] args) {
        DecodeString sol = new DecodeString();
        String s1 = "10[a]";
        String s2 = "3[a2[c]]";
        System.out.println(sol.decodeString(s1));
        System.out.println(sol.decodeString2(s1));
        // System.out.println(sol.decodeString(s2));
    }
}
