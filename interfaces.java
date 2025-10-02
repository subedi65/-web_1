 interface Animal {
    void sound();
  }
 class Dog implements Animal {
    public void sound(){
        System.out.println("woof");
    }
 }
 public class interfaces{
    public static void main(String[]args){
        Dog myDog = new Dog();
        myDog.sound();
    }
 }
 