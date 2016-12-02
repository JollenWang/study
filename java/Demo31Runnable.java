class MyThread implements Runnable {
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

public class Demo31Runnable {
    public static void main(String[] args) {
        MyThread t0 = new MyThread("T");
        
        new Thread(t0).start();
        new Thread(t0).start();
        new Thread(t0).start();
    }
}
