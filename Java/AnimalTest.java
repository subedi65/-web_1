

// abstract method in java

abstract class Animal{
    //abstract method (no implementation)
    public abstract void sound();
}
class Dog extends Animal {
@Override
    public void sound(){
        System.out.println("woof");
    }
}
public class AnimalTest{
    public static void main(String[] args) {
        Animal mydog = new Dog();
        mydog.sound();
    }
}