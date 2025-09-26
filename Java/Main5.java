//consturctor example
public class Main5{
    int modelYear;
    String modelName;
    public Main5(int Year ,String name){
        modelYear = Year;
        modelName = name;

    }
    public static void main(String[] args) {
        Main5 myCar = new Main5(1900,"mustang");
        System.out.println(myCar.modelYear + " "+ myCar.modelName);
    }
}


