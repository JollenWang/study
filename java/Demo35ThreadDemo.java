class MyThread extends Thread {
    private int time;
    public MyThread(String name, int time) {
        super(name);
        this.time = time;
    }

    public void run() {
        System.out.println(Thread.currentThread().getName() + "sleep" + this.time + "ms");
        try {
            Thread.sleep(this.time);
        } catch(Exception e) {
            e.printStackTrace();
        }
        System.out.println(Thread.currentThread().getName() + "sleep done.");
    }
}

public class Demo35ThreadDemo {
    public static void main(String[] args) {
        MyThread m0 = new MyThread("T0", 6000);
        MyThread m1 = new MyThread("T1", 3000);
        MyThread m2 = new MyThread("T2", 1000);

        m0.start();
        m1.start();
        m2.start();
    }
}
