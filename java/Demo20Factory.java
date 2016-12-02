interface Fruit {
    public void eat();
}

class Apple implements Fruit {
    public void eat() {
        System.out.println("$>Eat Apple!");
    }
}

class Orange implements Fruit {
    public void eat() {
        System.out.println("$>Eat Orange!");
    }
}

class Factory {
    public static Fruit getInstanceByName(String className) {
        Fruit f = null;
        if ("Apple".equals(className))
            f = new Apple();

        if ("Orange".equals(className))
            f = new Orange();
        return f;
    }
}

public class Demo20Factory {
    public static void main(String[] args) {
        System.out.println("$>prefix= " + args[0] + " fruit= " + args[1]);
        
        //Factory f = new Factory();
        //f.getInstanceByName(args[1]).eat();
        Fruit f = Factory.getInstanceByName(args[1]);
        f.eat();
    }
}

