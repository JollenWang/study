class MyThread implements Runnable {
    private String name;

    public MyThread(String name) {
        this.name = name;
    }

    public void run() {
        for (int i = 0 ; i < 10; i++)
            System.out.println(name + " run " + i);
    }
}

public class Demo29Runnable {
    public static void main(String[] args) {
        MyThread A = new MyThread("A");
        MyThread B = new MyThread("B");
        Thread T1 = new Thread(A);
        Thread T2 = new Thread(B);

        T1.start();
        T2.start();
    }
}
