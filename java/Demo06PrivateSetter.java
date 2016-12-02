class Person2 {
    private String name;
    private int age;

    public void tell() {
        System.out.println("Name:" + name + " Age:" + age);
    }

    public void setName(String n) {
        name = n;
    }

    public void setAge(int a) {
        age = a;
    }
}

public class Demo06PrivateSetter 
{
    public static void main(String[] args) {
        Person2 per = new Person2();

        per.setName("Jollen");
        per.setAge(30);
        per.tell();
    }
}

