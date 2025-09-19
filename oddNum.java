public class oddNum {

    public static void main(String[] args) {
        System.out.println("The Odd numbers are:");
        for (int i =1 ;i<=100; i++){
            if (i%2!=0){
                System.out.println(i+" ");
            }
        }
    }
}
class sumOddNum{
    public static void main(String[] args) {
        System.out.println("The sum of odd number are :");
        int sum = 0;
        for (int i =1; i<=100;i++)
        {
            if (i%2!=0)
            {
                sum = sum + i;
            }
        }System.out.println("the sum of odd numbers are :"+ sum);
    }

}