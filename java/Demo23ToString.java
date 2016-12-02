class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String toString() {
        return "Name= " + this.name + " Age= " + this.age;
    }
}

public class Demo23ToString {
    public static void main(String[] args) {
        Person p = new Person("Jollen", 32);
        System.out.println(p);
    }
}
