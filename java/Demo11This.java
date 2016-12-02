class Person {
    private String name;
    private int age;
    
    public Person() {
        System.out.println("A new Person class created.");
    }

    public Person(String name, int age) {
        this();
        this.setName(name);
        this.setAge(age);
    }

    public void setName(String n) {
        name = n;
    }

    public void setAge(int a) {
        this.age = a;
    }

    public void getInfo() {
        System.out.println("Name = " + name + " Age = " + age);
    }
}

public class Demo11This {
    public static void main(String[] args) {
        Person per = new Person("Jollen", 32);
        per.getInfo();
    }
}

