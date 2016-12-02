class nPerson {
    private String name;
    private int age;
    private String sex;
    public void tell() {
        System.out.println("Name=" + name + " Age=" + age + " Sex=" + sex);
    }
}

public class Demo05ErrRef {
    public static void main(String[] args) {
        nPerson per = new nPerson();
        per.name = "Jollen";
        per.age = 30;
        per.tell();
    }
}
