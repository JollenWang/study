class myPerson {
    private String name;
    private int age;
    public myPerson(){};

    public myPerson(String name) {
        this.setName(name);
    }

    public myPerson(String name, int age) {
        this.setName(name);
        this.setAge(age);
    }

    public void tell() {
        //System.out.println("Name=" + getName() + " Age=" + getAge());
        //System.out.println("Name=" + this.getName() + " Age=" + this.getAge());
        System.out.println("Name=" + name + " Age=" + age);
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public void setName(String n) {
        name = n;
    }

    public void setAge(int a) {
        age = a;
    }

}

public class Demo08ConsReload {
    public static void main(String[] args) {
        new myPerson("Jollen", 20).tell();
        myPerson per = new myPerson("Jollen", 21);
        per.tell();

        myPerson per2 = new myPerson("Jollen2");
        per2.tell();

        myPerson per3 = new myPerson();
        per3.tell();
    }
}
