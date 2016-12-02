class Singleton {
    static Singleton instence = new Singleton();
    private Singleton() {
    }

    public void print() {
        String str = "Good luck!";
        System.out.println(str);
    }
}

public class Demo14Singleton {
    public static void main(String[] args) {
        Singleton s1 = Singleton.instence;
        s1.print();
    }
}
