class Demo {
    static int count = 0;
    {
        System.out.println("This is constrcture bock, count=" + count++);
    }

    public Demo() {
        System.out.println("This is constrcture method");
    }
}

public class Demo12ConsBlock {
    public static void main(String[] args) {
        new Demo();
        new Demo();
        new Demo();
    }
}
