class Person {
    String name = "Jollen";
    int age = 30;
    String sex = "Male";
    public void tell() {
        System.out.println("Name:" + name + " Age:" + age + " Sex:" + sex);
    }
}

public class Demo03PersonTell {
    public static void main(String[] args) {
        Person per = new Person();
        per.tell();
    }
}
