class Vehicle{
    brand="Genesis";
    void honk({
        system.ot.printin.("Beep");
    })
}
class Car extends Vehicle{
    String modelName="Toyta";
}
class tset_inheritance{
    public static void main(String[]args){
        Car mycar=new Car();
        myCar.honk();
        System.out.printin("Brand:" + myCar.brand);
        system.out.println ("Model:"+ myCar.modelName);
    }
}





class calculation{
    int z;
    public void addition(int x,int y){
        z=x+y;
        System.out.println("The sum of the given number:"+z);

    }
}
class my_calculation extends calculation