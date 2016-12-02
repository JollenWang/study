class MyThread extends Thread {
    private String name;
    private int ticket = 5;

    public MyThread(String name) {
        this.name = name;
    }

    public void run() {
        for (int i = 0; i < 100; i++) {
            if (ticket > 0)
                System.out.println(this.name + " has " +  ticket-- + " tickets left");
        }
    }
}

public class Demo30Thread {
    public static void main(String[] args) {
        MyThread t0 = new MyThread("T0");
        MyThread t1 = new MyThread("T1");
        MyThread t2 = new MyThread("T2");

        t0.start();
        t1.start();
        t2.start();
    }
}
