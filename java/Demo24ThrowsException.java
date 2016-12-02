class Math {
    public int div(int i, int j) throws Exception {
        return i / j;
    }
}

public class Demo24ThrowsException {
    public static void main(String[] args)
    {
        Math m = new Math();
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        try {
            System.out.println(a + " / " + b + " = " + m.div(a, b));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
