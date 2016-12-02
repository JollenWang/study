class MyThread implements Runnable {
    public void run() {
        for (int i = 0; i < 20; i++) {
            System.out.println("My" + " run " + i);
            try {
                Thread.sleep(300);
            } catch(Exception e) {}
        }
    }
}

public class Demo32ThreadJoin {
    public static void main(String[] args) {
        MyThread my = new MyThread();
        Thread t = new Thread(my, "user");

        t.start();
        for (int i = 0; i < 30; i++) {
            if (i > 10) {
                try {
                    t.join();
                } catch(Exception e) {}
            }
            //System.out.println(Thread.currentThread.getName() + "run " + i);
            System.out.println("Main " + i);
        }
    }
}

