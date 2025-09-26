class account{
    int acc_no;
    String name;
    float amount;
    //method to initialize object
    void insert (int a, String n, float amt){
        acc_no =a;
        name = n;
        amount = amt;
    }
    //deposit method
    void deposit(float amt){
        amount = amount+ amt;
        System.out.println(amt + "deposited");
    }
    //withdraw method
    void withdraw(float amt){
        if(amount<amt){
            System.out.println("insufficient balance");
        }
        else{
            amount = amount-amt;
            System.out.println(amt +"withdrawn");
        }
    }
    //method to check the balance of the account
    void checkBalance(){
        System.out.println("balance is :"+ amount);
    }
    //method to display the values of the object
    void display(){
        System.out.println(acc_no + ""+name + " "+ amount);
    }
}
 class bankingSystem{
    public static void main(String[]args){
        account a1 = new account();
        a1.insert(82154,"kim",1000);
        a1.display();
        a1.checkBalance();
        a1.deposit(40000);
        a1.checkBalance();
        a1.withdraw(1000);

    }
}
