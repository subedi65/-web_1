public class person{
    privete Strin name;//privet=restricted access
    //Getter 
    public Strin getName(){
        return name;
    }
//setter
public void setName(Strin newName){
    this.name=newName;

} }
public class Main{
    public static void main(steing[]args){
        Person myObj= new Person();
        myObj.name="Jone";//error
    }
}