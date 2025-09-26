// Final method in java


class Animal {
    // final method (cannot be written)
    public static void sound(){
        System.out.println("some sound");
    }
    }
class Dog extends Animal{
    //invalid : cannot override a final method
    public void sound(){
        System.out.println("Woof!");

}
public class Animaltest2{
    public static void main(String[] args) {
        
    }
}