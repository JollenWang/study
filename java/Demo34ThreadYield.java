class MyThread implements Runnable {
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println(Thread.currentThread().getName() +  " run: " + i);
            if (i == 3) {
                System.out.print(">task yield.");
                Thread.currentThread().yield();
            }
        }
    }
}

public class Demo34ThreadYield {
    public static void main(String[] args) {
        MyThread m = new MyThread();
        Thread t0 = new Thread(m, "Task 0");
        Thread t1 = new Thread(m, "Task 1");

        t0.start();
        t1.start();
    }
}
