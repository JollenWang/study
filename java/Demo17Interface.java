interface A {
    public static final String AUTHOR = "Jollen";
    public void print();
    public String getInfo();
}

interface B {
    public void say();
}

class X implements A, B {
    public void say() {
        System.out.println("$>Hello World!");
    }

    public void print() {
        System.out.println("AUTHOR=" + this.getInfo());
    }

    public String getInfo() {
        return AUTHOR;
    }
}

public class Demo17Interface {
    public static void main(String[] args) {
        X x = new X();
        x.say();
        x.print();
    }
}

