 //synchronized method in java



class Counter{
    private int count = 0;
    //synchronized method
    public synchronized void increment(){
        count ++;
    }
    public synchronized int getCount(){
        return count;
    }
}

public class Main3 {
    public static void main(String[] args) {
        counter counter = new Counter();
        //you can now safely use the synchronized method in multi threaded eniveronments
    }
    
}
