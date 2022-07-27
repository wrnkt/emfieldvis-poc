public class MagFieldCalculator
{
    private int numberCalls;
    private double muo = Math.PI*4e-7;

    public MagFieldCalculator() {
        this.numberCalls = 0;
        System.out.println("new Magnetic Field Calculator instantiated");
    }

    public int returnCalls() {
        return this.numberCalls;
    }

    public double radiusFromCurrentAndField(double current, double b){
        numberCalls++;
        double radius = (muo*current)/(2*Math.PI*b);
        System.out.println(returnCalls());
        return radius;
    }

    public double fieldFromCurrentAndRadius(double current, double radius){
        numberCalls++;
        double b = (muo*current)/(2*Math.PI*radius);
        return b;
    }

    public double currentFromRadiusAndField(double radius, double field) {
        numberCalls++;
        double current = (2*Math.PI*field*radius)/(muo);
        return current;
    }

}
