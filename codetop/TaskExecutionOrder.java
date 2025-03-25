import java.util.concurrent.*;

public class TaskExecutionOrder {

    public static void main(String[] args) {
        ExecutorService customExecutor = Executors.newFixedThreadPool(3); // 创建线程池

        CompletableFuture<Void> task1 = CompletableFuture.runAsync(() -> {
            System.out.println("Task 1 started");
            try {
                Thread.sleep(1000); // 模拟任务执行
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println("Task 1 completed");
        }, customExecutor);

        CompletableFuture<Void> task2 = CompletableFuture.runAsync(() -> {
            System.out.println("Task 2 started");
            try {
                Thread.sleep(1000); // 模拟任务执行
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println("Task 2 completed");
        }, customExecutor);

        CompletableFuture<Void> task3 = CompletableFuture.runAsync(() -> {
            System.out.println("Task 3 started");
            try {
                Thread.sleep(1000); // 模拟任务执行
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println("Task 3 completed");
        }, customExecutor);

        CompletableFuture<Void> task4 = CompletableFuture.runAsync(() -> {
            System.out.println("Task 4 started");
            try {
                Thread.sleep(1000); // 模拟任务执行
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println("Task 4 completed");
        }, customExecutor);

        // 等待所有任务完成
        CompletableFuture.allOf(task1, task2, task3, task4).join();

        customExecutor.shutdown(); // 关闭线程池
    }
}
