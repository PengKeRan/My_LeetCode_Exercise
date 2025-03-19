import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.Lock;

public class deadLock {

    private static final Lock lock1 = new ReentrantLock();
    private static final Lock lock2 = new ReentrantLock();

    public static void main(String[] args) {
        // 死锁示例代码
        // Thread th1 = new Thread(() -> {
        // System.out.println(Thread.currentThread() + " start");
        // synchronized (lock1) {
        // System.out.println(Thread.currentThread() + " get lock1,waiting lock2");
        // try {
        // Thread.sleep(10);
        // } catch (InterruptedException e) {
        // e.printStackTrace();
        // }
        // synchronized (lock2) {
        // System.out.println(Thread.currentThread() + " get lock2");
        // }
        // }
        // System.out.println(Thread.currentThread() + " finished");
        // });
        // Thread th2 = new Thread(() -> {
        // System.out.println(Thread.currentThread() + " start");
        // synchronized (lock2) {
        // System.out.println(Thread.currentThread() + " get lock2,waiting lock1");
        // try {
        // Thread.sleep(10);
        // } catch (InterruptedException e) {
        // e.printStackTrace();
        // }
        // synchronized (lock1) {
        // System.out.println(Thread.currentThread() + " get lock1");
        // }
        // }
        // System.out.println(Thread.currentThread() + " finished");
        // });

        // 死锁解决
        Thread th1 = new Thread(() -> {
            System.out.println(Thread.currentThread() + " start");
            while (true) {
                if (lock1.tryLock()) {
                    try {
                        System.out.println(Thread.currentThread() + " Holding lock 1...");
                        try {
                            Thread.sleep(5000);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        System.out.println(Thread.currentThread() + " Waiting for lock 2...");
                        if (lock2.tryLock()) {
                            try {
                                System.out.println(Thread.currentThread() + " Acquired lock 2!");
                                break;
                            } finally {
                                lock2.unlock();
                            }
                        }
                    } finally {
                        lock1.unlock();
                    }
                }
                try {
                    Thread.sleep(5000); // 重试前等待
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            System.out.println(Thread.currentThread() + " finished");
        });
        Thread th2 = new Thread(() -> {
            System.out.println(Thread.currentThread() + " start");
            while (true) {
                if (lock2.tryLock()) {
                    try {
                        System.out.println(Thread.currentThread() + " Holding lock 2...");
                        try {
                            Thread.sleep(5000);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        System.out.println(Thread.currentThread() + " Waiting for lock 1...");
                        if (lock1.tryLock()) {
                            try {
                                System.out.println(Thread.currentThread() + " Acquired lock 1!");
                                break;
                            } finally {
                                lock1.unlock();
                            }
                        }
                    } finally {
                        lock2.unlock();
                    }
                }
                try {
                    Thread.sleep(5000); // 重试前等待
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            System.out.println(Thread.currentThread() + " finished");
        });
        // th1.start();
        // th2.start();

        CompletableFuture<Void> future1 = CompletableFuture.runAsync(() -> {
            System.out.println(Thread.currentThread() + "running 1");
        });
        CompletableFuture<Void> future2 = future1.thenRun(() -> {
            System.out.println(Thread.currentThread() + "running 2");
        });
        CompletableFuture<Void> future3 = future2.thenRun(() -> {
            System.out.println(Thread.currentThread() + "running 3");
        });

        try {
            future3.get();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
