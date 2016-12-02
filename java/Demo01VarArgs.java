public class Demo01VarArgs {
    public static void main(String[] args) {
        System.out.print("fun():");
        fun();
        System.out.print("\nfun(1):");
        fun(1);
        System.out.print("\nfun(1,5,7)");
        fun(1, 5, 7);
        System.out.print('\n');
    }

    public static void fun(int... arg) {
        for (int i : arg)
            System.out.print(i+ ",");
    }
}
