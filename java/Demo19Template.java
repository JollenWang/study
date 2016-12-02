abstract class Person {
    private String name;
    private int age;

    public Person(String name, int age)
    {
        this.name = name;
        this.age = age;
    }

    public String getName()
    {
        return name;
    }

    public int getAge()
    {
        return age;
    }

    public void tellInfo()
    {
        System.out.println(this.tellContent());
    }

    public abstract String tellContent();
}

class Student extends Person {
    private float score;
    private String school;

    public Student(String name, int age, String school, float score)
    {
        super(name, age);
        this.school = school;
        this.score = score;
    }

    public String tellContent()
    {
        return "Name= " + super.getName() + " Age= " + super.getAge() + 
               " School= " + this.school + " Score= " +  this.score;
    }
}

class Worker extends Person {
    private float salary;
    private String company;

    public Worker(String name, int age, String company, float salary)
    {
        super(name, age);
        this.company = company;
        this.salary = salary;
    }

    public String tellContent()
    {
        return "Name= " + super.getName() + " Age= " + super.getAge() + 
                " Company= " + this.company + " Salary= " + this.salary;
    }
}

public class Demo19Template {
    public static void main(String[] args)
    {
        Student s = new Student("Alex", 20, "MIT", 99.0f);
        Worker w = new Worker("Tom", 30, "Sun", 5000.00f);

        s.tellInfo();
        w.tellInfo();
    }
}

