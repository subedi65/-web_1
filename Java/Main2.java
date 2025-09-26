//  use of static method



class MathUtil{
    //static method
    public static int add(int a, int b){
        return a+b;
    }
}



public class Main2 {
    public static void main(String[] args) {
        int result = MathUtil.add(5,3);//calling static method without the object
        System.out.println(result);
    }
}
