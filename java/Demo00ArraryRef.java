public class Demo00ArraryRef {
    public static void main(String[] args) {
        int tmp[] = fun();
        print(tmp);
    }

    public static void print(int x[]) {
        for (int i = 0; i < x.length; i++)
            System.out.print(x[i] + " ");
        System.out.println("");
    }

    public static int[] fun() {
        int buf[] = {1,4,67,52};
        return buf;
    }
}
