public class day{

    public static void main(String[] args) {
        var x = 5;
        var y = 9.99;
        var mychar = 'D';
        var myboolean = true;
        var mystring = "hello";
        System.out.println(x);
        System.out.println(y);
        System.out.println(mychar);
        System.out.println(myboolean);
        System.out.println(mystring);

        day1.main(args);
        day2.main(args);
        day3.main(args);

    }
}
 class day1{
    public static void main(String[] args) {
        char a = 'G';
        int i = 89;
        byte b = 4;
        short s = 56;
        double d = 4.55151;
        float f = 4.74541f;
        long l = 12121;
        System.out.println("char :" + a);
        System.out.println("integer :" + i);
        System.out.println("byte : " + b);
        System.out.println("short :" + s);
        System.out.println("float :" + f);
        System.out.println("double :" + d);
        System.out.println("long :" + l);

        
    }
}
class day2{
    public static void main(String[] args) {
        double pi = 3.141592653;
        double an = 6.0221407e23;
        System.out.println("value of Pi :" + pi);
        System.out.println(" value of Avogadro'S :" + an);
    }
}
class day3{
    public static void main(String[] args) {
        String n = "Elly";
        String m = "Hello , Welcome to java class";
        System.out.println("Name :" + n);
        System.out.println("Message :" + m);
        
    }
}