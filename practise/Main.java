interface Account {
    void Account_deposit(double amount);
    void Account_withdraw(double amount);
}

class Account_Bank implements Account {
    private double balance;

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public void Account_deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: " + amount + ", New balance: " + balance);
    }

    public void Account_withdraw(double amount) {
        balance -= amount;
        System.out.println("Withdrawn: " + amount + ", New balance: " + balance);
    }
}

class Account_Savings extends Account_Bank {
    @Override
    public void Account_withdraw(double amount) {
        if (amount <= getBalance()) {
            super.Account_withdraw(amount);
        } else {
            System.out.println("Withdrawal denied: Insufficient balance!");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Account_Savings acc = new Account_Savings();
        acc.Account_deposit(400000);
        acc.Account_withdraw(500);
        acc.Account_withdraw(8000000);
    }
}