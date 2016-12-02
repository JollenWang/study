abstract class A {
    public static final String FLAG = "CHINA";
    private String name = "Jollen";
    
    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public abstract void print();
}

class B extends A {
    public void print() {
        System.out.println("FLAG=" + FLAG);
        System.out.println("Name=" + super.getName());
    }
}

public class Demo15Abstract {
    public static void main(String[] args) {
        B b = new B();
        b.setName("Pony");
        b.print();
    }
}
