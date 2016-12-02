abstract class Person {
    private String name = "Jollen";
    private int age = 30;
    public Person(String name, int age) {
        this.setName(name);
        this.setAge(age);
    }

    public void setName(String name) {
        this.name = name;
        //name = name;
    }

    public String getName() {
        return this.name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getAge() {
        return this.age;
    }

    public abstract String getInfo();
}

class Student extends Person {
    private String school;
    public Student(String name, int age, String school) {
        super(name, age);
        this.setSchool(school);
    }

    public void setSchool(String school) {
        this.school = school;
    }

    public String getSchool() {
        return this.school;
    }

    public String getInfo() {
        return "Name: " + super.getName() + " Age: " + super.getAge() + " School: " + this.getSchool();
    }
}

public class Demo16SuperAbstract {
    public static void main(String[] args) {
        Student s = new Student("Alx", 32, "MIT");
        System.out.println(s.getInfo());
    }
}


