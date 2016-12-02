class MyThread implements Runnable {
    public void run() {
        System.out.println("1>task enter.");
        try {
            Thread.sleep(3000);
            System.out.println("2>task sleep done.");
        } catch(Exception e) {
            System.out.println("3>task interrupted.");
            return;
        }

        System.out.println("4>task return OK.");
    }
}

public class Demo33ThreadInterrupt {
    public static void main(String[] args) {
        MyThread my = new MyThread();
        Thread t = new Thread(my, "USER");

        t.start();
        try {
            Thread.sleep(1500);
        } catch(Exception e) {}
        t.interrupt();
    } 
}
