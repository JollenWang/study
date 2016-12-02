class MyThread extends Thread {
    private String name;
    public MyThread(String name) {
        this.name = name;
    }

    public void run() {
        for (int i = 0; i < 10; i++)
            System.out.println(this.name + " run " + i);
    }
}

public class Demo28Thread {
    public static void main(String[] args) {
/*
         MyThread A = new MyThread("Thread A");
        MyThread B = new MyThread("Thread B");
        A.start();
        B.start();
*/

        new MyThread("A").start();
        new MyThread("B").start();
    }
}
