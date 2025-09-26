//java program to demonstrate the use of parameterized constructor

 class Student4 {
    int id;
    String name;
    //creating a parameterized constuctor
    Student4(int i, String n){
        id = i;
        name =n;

    }
    //method to display the values void display()
    void display(){
        System.out.println(id +"" + name);
    }
    public static void main(String[] args) {
        //creating objects and passing valyues
        Student4 s1 = new Student4(111, "aryan");
        //calling method to display the values of object
        s1.display();
        s2.display();
    }
}
