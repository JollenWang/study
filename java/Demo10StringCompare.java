public class Demo10StringCompare {
    public static void main(String[] args) {
        String s0 = "Hello";
        String s1 = "Hello";
        String s2 = new String("Hello");
        String s3 = new String("Hello");

        boolean f0 = s0.equals(s1);
        boolean f1 = s0.equals(s2);
        boolean f2 = s2.equals(s3);
        boolean f3 = "Hello".equals("Hello");

        System.out.println("s0 == s1 is " + (s0 == s1));
        System.out.println("s0 == s2 is " + (s0 == s2));
        System.out.println("s2 == s3 is " + (s2 == s3));
        System.out.println("\"Hello\" == \"Hello\"-->" +  ("Hello" == "Hello") + "\n");

        System.out.println("s0 equals to s1 is " + f0);
        System.out.println("s0 equals to s2 is " + f1);
        System.out.println("s2 equals to s3 is " + f2);
        System.out.println("\"Hello\" is equal to \"Hello\"-->" +  f3);
    }
}
