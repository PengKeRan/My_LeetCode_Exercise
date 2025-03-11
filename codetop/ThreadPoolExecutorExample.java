import java.util.concurrent.*;

public class ThreadPoolExecutorExample {
    public static void main(String[] args) {
        // 创建 ThreadPoolExecutor
        ThreadPoolExecutor executor = new ThreadPoolExecutor(
                2, // 核心线程数
                4, // 最大线程数
                60, // 空闲线程存活时间
                TimeUnit.SECONDS, // 时间单位
                new LinkedBlockingQueue<>(10), // 任务队列
                Executors.defaultThreadFactory(), // 线程工厂
                new ThreadPoolExecutor.AbortPolicy() // 拒绝策略
        );

        // 提交任务到线程池
        for (int i = 1; i <= 10; i++) {
            Task task = new Task("Task " + i);
            System.out.println("Submitting " + task.getName());
            executor.execute(task);
        }

        // 关闭线程池
        executor.shutdown();
    }
}

// 定义一个简单的任务类
class Task implements Runnable {
    private String name;

    public Task(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public void run() {
        System.out.println(name + " is running on thread " + Thread.currentThread().getName());
        try {
            // 模拟任务执行时间
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(name + " has completed.");
    }
}