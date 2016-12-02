interface A {
    public String author = "Jollen";
    public void print();
    public String getInfo();
}

abstract class B {
    public abstract void say();
}

class C extends B implements A {
    public void say() {
        System.out.println("$>Hello World!");
    }

    public String getInfo() {
        return author;
    }

    public void print() {
        System.out.println("AUTHOR=" + this.getInfo());
    }
}

public class Demo18Extends {
    public static void main(String[] args) {
        C c = new C();
        c.say();
        c.print();
    }
}

