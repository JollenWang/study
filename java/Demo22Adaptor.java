interface Window {
    public void open();
    public void close();
    public void activated();
    public void configed();
    public void unconfiged();
}

abstract class Adaptor implements Window{
    public void open() {};
    public void close() {};
    public void activated() {};
    public void configed() {};
    public void unconfiged() {};
}

class RealWindow extends Adaptor {
    public void open() {
        System.out.println("$>Window is opened!");
    }

    public void close() {
        System.out.println("#>Window is closed!");
    }
}

public class Demo22Adaptor {
    public static void main(String[] args) {
        //RealWindow real = new RealWindow();
        Window real = new RealWindow();

        real.open();
        real.close();
    }
}

