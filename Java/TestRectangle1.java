 class rectangle{
    int length;
    int width;
    void insert(int l,int w){
        length = l;
        width = w;
    }
    void calculateArea()
    {
        System.out.println(length*width);}
    }

class TestRectangle1{
    public static void main(String[] args) {
        rectangle r1 = new rectangle();
        rectangle r2 =  new rectangle();
        // r1.insert(11,5);
        // r2.insert(3,15);
        r1.length = 11;
        r1.width = 5;
        r2.length = 3;
        r2.width = 15;
        r1.calculateArea();
        r2.calculateArea();
    }
}