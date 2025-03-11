import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = in.nextLong();
        }

        // 预处理每个数的质因数分解
        Map<Long, Long>[] factorMaps = new HashMap[n];
        for (int i = 0; i < n; i++) {
            factorMaps[i] = getPrimeFactors(arr[i]);
        }

        // 查找满足条件的三元组
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                Map<Long, Long> combined = new HashMap<>(factorMaps[i]);
                for (Map.Entry<Long, Long> entry : factorMaps[j].entrySet()) {
                    combined.merge(entry.getKey(), entry.getValue(), (v1, v2) -> (v1 + v2) % 2);
                }
                for (int k = j + 1; k < n; k++) {
                    Map<Long, Long> temp = new HashMap<>(combined);
                    for (Map.Entry<Long, Long> entry : factorMaps[k].entrySet()) {
                        temp.merge(entry.getKey(), entry.getValue(), (v1, v2) -> (v1 + v2) % 2);
                    }
                    if (temp.values().stream().allMatch(v -> v == 0)) {
                        System.out.println(i + " " + j + " " + k);
                        return;
                    }
                }
            }
        }
        System.out.println("-1");
    }

    private static Map<Long, Long> getPrimeFactors(Long num) {
        Map<Long, Long> factors = new HashMap<>();
        for (Long i = 2L; i * i <= num; i++) {
            while (num % i == 0) {
                factors.put(i, factors.getOrDefault(i, 0L) + 1L);
                num /= i;
            }
        }
        if (num > 1) {
            factors.put(num, 1L);
        }
        return factors;
    }
}
